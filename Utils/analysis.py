import re
import matplotlib.pyplot as plt

def plot_scores_from_log(log_file_path):
    # Open the log file
    with open(log_file_path, 'r') as file:
        lines = file.readlines()

    episodes = []
    scores = []

    # Extract episode numbers and scores using regex
    for line in lines:
        match = re.search(r"Episode (\d+) score: ([\d\.]+)", line)
        if match:
            episode = int(match.group(1))
            score = float(match.group(2))
            episodes.append(episode)
            scores.append(score)

    # Plot the scores
    plt.figure(figsize=(10, 6))
    plt.plot(episodes, scores, marker='o', linestyle='-', label='Episode Scores')
    plt.title('Episode Scores Over Time')
    plt.xlabel('Episode')
    plt.ylabel('Score')
    plt.grid(True)
    plt.legend()
    plt.show()

