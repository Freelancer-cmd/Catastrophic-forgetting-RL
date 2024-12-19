from Utils.config import ENV_CONFIG, AGENT_CONFIG
from rl_agents.agents.common.factory import load_environment, load_agent
import matplotlib.pyplot as plt

if __name__ == "__main__":

    print("---------- Executing main.py ----------")

    env = load_environment(ENV_CONFIG)
    print("Environment loaded")

    agent = load_agent(AGENT_CONFIG, env)
    print("Agent loaded")

    