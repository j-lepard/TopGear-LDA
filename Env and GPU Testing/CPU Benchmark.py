import numpy as np
import time

# CPU benchmark: Matrix multiplication
def cpu_benchmark():
    size = 10000
    A = np.random.rand(size, size)
    B = np.random.rand(size, size)
    
    start_time = time.time()
    C = np.dot(A, B)
    end_time = time.time()
    
    print(f"CPU Benchmark: {end_time - start_time} seconds")

cpu_benchmark()