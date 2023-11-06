import ml_collections

from sade.configs.ve.biggan_config import get_config as get_default_config


def get_config():
    config = get_default_config()

    config.training.batch_size = 64
    config.training.log_freq = 5
    config.training.use_fp16 = True

    config.eval.batch_size = 64

    # flow-model
    flow = config.flow
    flow.base_distribution = "multivariate_normal"
    flow.num_blocks = 20
    flow.context_embedding_size = 128
    flow.use_global_context = True
    flow.global_embedding_size = 512
    flow.input_norm = False

    flow.patch_batch_size = 32
    flow.patches_per_train_step = 256
    flow.training_kimg = 50

    # Config for patch sizes
    flow.local_patch_config = ml_collections.ConfigDict()
    flow.local_patch_config.kernel_size = 3
    flow.local_patch_config.padding = 1
    flow.local_patch_config.stride = 1

    # Config for larger receptive fields outputting gobal context
    flow.global_patch_config = ml_collections.ConfigDict()
    flow.global_patch_config.kernel_size = 17
    flow.global_patch_config.padding = 0
    flow.global_patch_config.stride = 8

    return config
