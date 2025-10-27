import matplotlib.pyplot as plt

def plot_convergence(history):
    plt.figure(figsize=(8, 5))
    plt.plot(history, marker='o', color='blue', linestyle='-', linewidth=1)
    plt.title("PSO Convergence Curve", fontsize=14)
    plt.xlabel("Iteration", fontsize=12)
    plt.ylabel("Best Fitness Value", fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.tight_layout()
    plt.savefig("convergence_plot.png")  # saves the plot
    plt.show()  # displays the plot window
