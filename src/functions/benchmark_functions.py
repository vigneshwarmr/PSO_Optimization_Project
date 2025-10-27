"""
benchmark_functions.py
----------------------
Contains common mathematical benchmark functions used in optimization.
"""

import math

def sphere_function(position):
    """Simple convex function (minimum at origin)."""
    return sum(x ** 2 for x in position)

def rastrigin_function(position):
    """Non-convex function with many local minima."""
    A = 10
    return A * len(position) + sum(x ** 2 - A * math.cos(2 * math.pi * x) for x in position)

def rosenbrock_function(position):
    """The classic banana-shaped valley function."""
    return sum(100 * (position[i+1] - position[i]**2)**2 + (1 - position[i])**2 for i in range(len(position)-1))
