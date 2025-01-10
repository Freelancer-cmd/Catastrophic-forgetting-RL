import os
import torch

# -----------------------------------------
# Training configuration
# -----------------------------------------


# -----------------------------------------
# Main steps
# -----------------------------------------

# -----------------------------------------
# Paths 
# -----------------------------------------

LOG_PATH = os.path.join(os.path.dirname(os.path.dirname(__file__)), "Logs")
ENV_CONFIG = 'rl-agents/scripts/configs/HighwayEnv/env_obs_attention.json'  
AGENT_CONFIG = 'Utils/Architectures/convolutionNN.json'
LOG_PATH = 'out/HighwayEnv/DQNAgent/run_20250110-180255_21008/logging.1179206764352.21008.log'  # Replace with the actual path to your log file

# -----------------------------------------
# Parameters 
# -----------------------------------------

DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
#DEVICE = torch.device("cpu")

