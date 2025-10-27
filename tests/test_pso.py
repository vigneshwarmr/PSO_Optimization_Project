"""
test_pso.py
-----------
Unit tests for PSO algorithm.
"""

from src.algorithms.pso_algorithm import pso_optimize
from src.functions.benchmark_functions import sphere_function

def test_pso_basic():
    """Simple test to check if PSO finds near-zero for the sphere function."""
    best_position, best_value = pso_optimize(sphere_function, bounds=(-5, 5), max_iter=30)
    assert best_value < 1e-2, f"PSO did not converge properly, got {best_value}"
