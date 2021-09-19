import tensorflow as tf
import matplotlib.pyplot as plt
import numpy as np
import os
import json

AUTOTUNE = tf.data.experimental.AUTOTUNE


def create_ds(images, batch_size, seed=15):
    BUFFER_SIZE = images.shape[0]
    img_ds = tf.data.Dataset.from_tensor_slices(images)
    print('Total images: {}'.format(images.shape[0]))
    ds = img_ds.cache().shuffle(
            BUFFER_SIZE, seed=seed).batch(batch_size, 
                drop_remainder=True, 
                num_parallel_calls=AUTOTUNE).prefetch(AUTOTUNE)
    return ds

def save_hparams(hparams, model_dir, model_name):
    json_hparams = json.dumps(hparams)
    f = open(os.path.join(model_dir, '{}_hparams.json'.format(model_name)), 'w')
    f.write(json_hparams)
    f.close()

def load_hparams(model_dir, model_name):
    hparams_path = os.path.join(model_dir, '{}_hparams.json'.format(model_name))
    with open(hparams_path, 'r') as f:
        hparams = json.load(f)
    f.close()
    print('Loading hparams from {}'.format(hparams_path))
    return hparams
    
def generate_and_save_images(model, epoch, noise, direct):
    predictions = model(noise, training=False)
 
    predictions = tf.clip_by_value(predictions[0] * 127.5 + 127.5, 0.0, 255.0)
    predictions = tf.cast(predictions, tf.uint8)
    n = int(np.sqrt(predictions.shape[0]))
    fig = plt.figure(figsize=(n-1, n-1))
    for i in range(predictions.shape[0]):
        plt.subplot(n, n, i+1)
        plt.imshow(predictions[i, :, :, :])
        plt.axis('off')
    path = os.path.join(direct, '{:04d}.png'.format(epoch))
    plt.savefig(path)
    # Clear the current axes.
    plt.cla() 
    # Clear the current figure.
    plt.clf() 
    # Closes all the figure windows.
    plt.close('all')
    
def gradient_penalty(critic, real_samples, fake_samples):
    alpha = tf.random.uniform([real_samples.shape[0], 1, 1, 1], minval=0., maxval=1.)
    diff = fake_samples - real_samples
    interpolation = real_samples + alpha * diff

    with tf.GradientTape() as gradient_tape:
        gradient_tape.watch(interpolation)
        pred = critic(interpolation, training=True)

    gradients = gradient_tape.gradient(pred[0], [interpolation])[0]
    norm = tf.sqrt(tf.reduce_sum(tf.square(gradients), axis=[1, 2, 3]))
    gradient_penalty = tf.reduce_mean((norm - 1.0) ** 2)
    return gradient_penalty
