# TrGAN

Generation of CIFAR10 images based on TrGAN (hands-on):

## Dependencies

- Python 3.8
- Tensorfow 2.5

## Usage

### Train

1. Use `--dataset_path=<path>` to specify the dataset path (default builds CIFAR-10 dataset), and `--model_name=<name>` to specify the checkpoint directory name.

```
python train.py --dataset_path=<path> --model_name=<name>
```

### Hparams setting

Adjust hyperparameters in the `hparams.py` file.

### Tensorboard

Run `tensorboard --logdir ./`.

## Examples

- CIFAR-10 training progress

![](images/transgan_samples.gif "TransGAN on CIFAR-10")

## References

Code:

- This model depends on other files that may be licensed under different open source licenses.
- TransGAN uses [Differentiable Augmentation](https://arxiv.org/abs/2006.10738). Under BSD 2-Clause "Simplified" License.
- Small-TransGAN models are instances of the original TransGAN architecture with a smaller number of layers and lower-dimensional embeddings.

Implementation notes:

- Single layer per resolution Generator.
- Orthogonal initializer and 4 heads in both Generator and Discriminator.
- WGAN-GP loss.
- Adam with β1 = 0.0 and β2 = 0.99.
- Noise dimension = 64.
- Batch size = 64

## Licence

MIT
