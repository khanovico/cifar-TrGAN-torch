hparams = {'batch_size': 64,
           'noise_dim': 64,
           'g_dim': 256, # 1024
           'g_depth': [1, 1, 1], # [5, 4, 2]
           'g_heads': [4, 2, 1], # [2, 2, 2]
           'g_mlp': [512, 512, 512],
           'g_learning_rate': 0.0001,
           'g_beta_1': 0.0,
           'g_beta_2': 0.99,
           'd_dim': [64, 64], # [192, 192]
           'd_depth': [1, 1], # [3, 3]
           'd_heads': [2, 2, 2],
           'd_mlp': [256, 256, 256], # [512, 512, 512]
           'd_patch_size': 4, # 2
           'd_learning_rate': 0.0001,
           'd_beta_1': 0.0,
           'd_beta_2': 0.99,
           'd_steps': 2,
           'loss': 'hinge', # wgan
           'gp_weight': 1.0}
