import numpy as np
import time

# Memory bandwidth benchmark
def memory_bandwidth_benchmark():
    size = 100000000
    A = np.random.rand(size)
    
    start_time = time.time()
    B = A.copy()
    end_time = time.time()
    
    print(f"Memory Bandwidth Benchmark: {end_time - start_time} seconds")

memory_bandwidth_benchmark()