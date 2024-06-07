from pathlib import Path

GPU_BATCH_SIZE = 64
GRADIENT_BATCH_SIZE = 64
PATH_LENGTH_REGULIZER_FREQUENCY = 2
GRADIENT_ACCUMULATE_EVERY = 4 # unused if using run.py

CONDITION_ON_MAPPER = True
CHANNELS = 5
NETWORK_CAPACITY = 16
STYLE_DEPTH = 8
IMAGE_SIZE = 32
LATENT_DIM = 512
USE_BIASES = False

EXTS = ['jpg', 'png']
FOLDER = "./data/OITAVEN/"

HOMOGENEOUS_LATENT_SPACE = True
USE_DIVERSITY_LOSS = False
MIXED_PROBABILITY = 0.9

MOVING_AVERAGE_START = 4000
MOVING_AVERAGE_PERIOD = 200

EVALUATE_EVERY = 29 # 200 29
SAVE_EVERY = 58 # 250 58
NUM_TRAIN_STEPS = 250 # 10 200
VAL_SIZE = 1000 # 1000 non_usado

NAME = "default"
CURRENT_DIR = Path('.')

LOG_DIR = CURRENT_DIR / 'logs'
MODELS_DIR = CURRENT_DIR / 'models'
RESULTS_DIR = CURRENT_DIR / 'results'
LOG_DIR = CURRENT_DIR / 'logs'

VAL_FILENAME = CURRENT_DIR / 'val.csv'
TRAIN_FILENAME = CURRENT_DIR / 'train.csv'
LOG_FILENAME = CURRENT_DIR / 'logs.csv'

LOG_FILENAME = 'logs.csv'
VAL_FILENAME = 'val.csv'
TRAIN_FILENAME = 'train.csv'

NEW = True
LOAD_FROM = -1

GPU = '0'
EPSILON = 1e-8
LEARNING_RATE = 2e-4
LABEL_EPSILON = 0
