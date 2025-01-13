import os
import torch

# -----------------------------------------
# Training configuration
# -----------------------------------------

NUM_EP_TRAINING = 1500
NUM_EP_TEST = 150
EPISODE_LEN = 80


# -----------------------------------------
# Main steps
# -----------------------------------------

TRAINING = False
TEST = True

# -----------------------------------------
# Paths 
# -----------------------------------------

LOG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Logs")
ENV_CONFIG = 'Utils/Enviroments/env_obs_convolution.json'  
AGENT_CONFIG = 'Utils/Architectures/convolutionNN.json'
LOG_PATH = 'out/HighwayEnv/DQNAgent/run_20250110-180255_21008/logging.1179206764352.21008.log'  # Replace with the actual path to your log file
MODEL_PATH = 'Utils/Models/EGO.tar'

# -----------------------------------------
# Parameters 
# -----------------------------------------

DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
#DEVICE = torch.device("cpu")

