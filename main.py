print('Particle Swarm Optimization initialized')
"""
main.py
-------
Entry point for running PSO Optimization experiments.
"""

from src.algorithms.pso_algorithm import pso_optimize
from src.functions.benchmark_functions import sphere_function
from src.utils.helpers import load_config, timer

@timer
def main():
    config = load_config()

    best_pos, best_val = pso_optimize(
        objective_function=sphere_function,
        bounds=tuple(config["pso"]["bounds"]),
        num_particles=config["pso"]["num_particles"],
        dimensions=config["pso"]["dimensions"],
        max_iter=config["pso"]["max_iter"],
        inertia_weight=config["pso"]["inertia_weight"],
        cognitive_const=config["pso"]["cognitive_const"],
        social_const=config["pso"]["social_const"],
    )

    print(f"\n✅ Optimization Complete\nBest Position: {best_pos}\nBest Value: {best_val:.6f}")

if __name__ == "__main__":
    main()
