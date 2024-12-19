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
ENV_CONFIG = 'configs/HighwayEnv/env_obs_attention.json'  
AGENT_CONFIG = 'configs/HighwayEnv/agents/DQNAgent/ego_attention2Head.json'

# -----------------------------------------
# Parameters 
# -----------------------------------------

DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
#DEVICE = torch.device("cpu")