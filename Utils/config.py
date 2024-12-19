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
AGENT_CONFIG = 'Utils/Architectures/attentionNN.json'

# -----------------------------------------
# Parameters 
# -----------------------------------------

DEVICE = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
#DEVICE = torch.device("cpu")