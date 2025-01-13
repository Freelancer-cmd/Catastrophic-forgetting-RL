import sys
import os
import numpy as np
from Utils.config import ENV_CONFIG, AGENT_CONFIG, DEVICE, LOG_PATH, TRAINING, MODEL_PATH, NUM_EP_TRAINING, NUM_EP_TEST,EPISODE_LEN


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'rl-agents')))
from rl_agents.agents.common.factory import load_environment, load_agent
from scripts.experiments import evaluate
from rl_agents.trainer.evaluation import Evaluation

if __name__ == "__main__":

    print("---------- Executing main.py ----------")

    env = load_environment(ENV_CONFIG)
    print("Environment loaded")

    agent = load_agent(AGENT_CONFIG, env)
    print("Agent loaded")

    print("Device: ", DEVICE)

    if TRAINING == True:

        print("Training agent...")
        evaluate(ENV_CONFIG, AGENT_CONFIG, {'--train': TRAINING, '--test':not TRAINING, '--episodes': NUM_EP_TRAINING, '--recover': False, '--no-display': True, '--seed': 10, '--verbose': True, '--name-from-config': False, '--recover-from': False})
        print("Agent trained")
    
    else:
        print("Evaluating the agent...")
        num_failed_episodes = 0
        for ep in NUM_EP_TEST:
            ev = Evaluation(env, agent, num_episodes = 1, training = False, recover = MODEL_PATH)
            ev.test()
            states = ev.explain_dict['state']
            actions = ev.explain_dict['action']
            actions = np.array(actions)  
    
            num_of_frame = actions.shape[0]
            print(num_of_frame)
            if num_of_frame < EPISODE_LEN:
                print('Num of frames:', num_of_frame)
                num_failed_episodes = num_failed_episodes + 1

        print("Succes rate:", num_failed_episodes/NUM_EP_TEST)


    #print("Plotting scores...")
    #plot_scores_from_log(LOG_PATH)

    print("---------- End of main.py ----------")

