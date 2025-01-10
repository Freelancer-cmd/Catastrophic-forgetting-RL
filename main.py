import sys
import os
from Utils.config import ENV_CONFIG, AGENT_CONFIG, DEVICE
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'rl-agents')))
from rl_agents.agents.common.factory import load_environment, load_agent
from scripts.experiments import evaluate

if __name__ == "__main__":

    print("---------- Executing main.py ----------")

    env = load_environment(ENV_CONFIG)
    print("Environment loaded")

    agent = load_agent(AGENT_CONFIG, env)
    print("Agent loaded")

    print("Device: ", DEVICE)

    print("Evaluating agent...")
    evaluate(ENV_CONFIG, AGENT_CONFIG, {'--train': True, '--episodes': 2, '--recover': False, '--no-display': True, '--seed': 10, '--verbose': False, '--name-from-config': False, '--recover-from': False})
    print("Agent evaluated")

    print("---------- End of main.py ----------")

