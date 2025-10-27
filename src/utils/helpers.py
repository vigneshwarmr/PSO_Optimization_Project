"""
helpers.py
-----------
Utility functions for logging, config parsing, and timing.
"""

import yaml
import time

def load_config(path="config.yaml"):
    """Load experiment configuration."""
    with open(path, "r") as file:
        return yaml.safe_load(file)

def timer(func):
    """Decorator for timing functions."""
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"⏱ Execution time: {time.time() - start:.2f}s")
        return result
    return wrapper
