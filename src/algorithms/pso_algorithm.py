"""
pso_algorithm.py
----------------
Implements the core logic of the Particle Swarm Optimization (PSO) algorithm.
"""

import random
import math

class Particle:
    def __init__(self, dimensions, bounds):
        self.position = [random.uniform(bounds[0], bounds[1]) for _ in range(dimensions)]
        self.velocity = [random.uniform(-1, 1) for _ in range(dimensions)]
        self.best_position = list(self.position)
        self.best_value = float("inf")

    def __repr__(self):
        return f"Particle(pos={self.position}, best_val={self.best_value})"


def pso_optimize(objective_function, bounds, num_particles=30, dimensions=2, max_iter=100,
                 inertia_weight=0.5, cognitive_const=1.5, social_const=2.0):
    """Run the Particle Swarm Optimization algorithm."""
    swarm = [Particle(dimensions, bounds) for _ in range(num_particles)]
    global_best_value = float("inf")
    global_best_position = None

    for iteration in range(max_iter):
        for particle in swarm:
            value = objective_function(particle.position)
            if value < particle.best_value:
                particle.best_value = value
                particle.best_position = list(particle.position)
            if value < global_best_value:
                global_best_value = value
                global_best_position = list(particle.position)

        for particle in swarm:
            for d in range(dimensions):
                r1, r2 = random.random(), random.random()
                cognitive = cognitive_const * r1 * (particle.best_position[d] - particle.position[d])
                social = social_const * r2 * (global_best_position[d] - particle.position[d])
                particle.velocity[d] = inertia_weight * particle.velocity[d] + cognitive + social
                particle.position[d] += particle.velocity[d]

        print(f"Iteration {iteration + 1}/{max_iter}, Best Value = {global_best_value:.5f}")

    return global_best_position, global_best_value
