import matplotlib.pyplot as plt
import json

def plot_metrics(log_file="evaluation/logs.json"):
    with open(log_file) as f:
        data = json.load(f)

    lengths = [len(x["answer"]) for x in data]

    plt.plot(lengths)
    plt.title("Response Length Over Time")
    plt.xlabel("Query Index")
    plt.ylabel("Answer Length")
    plt.savefig("evaluation/performance.png")
