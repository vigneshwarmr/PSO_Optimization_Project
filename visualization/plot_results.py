"""
plot_results.py
---------------
Handles visualization of PSO results using matplotlib.
"""

import matplotlib.pyplot as plt

def plot_convergence(history):
    """Plot convergence curve."""
    plt.plot(history, marker='o')
    plt.title("PSO Convergence Curve")
    plt.xlabel("Iteration")
    plt.ylabel("Best Fitness Value")
    plt.grid(True)
    plt.show()
