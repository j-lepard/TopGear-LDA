import torch
import time

# GPU benchmark: Matrix multiplication
def gpu_benchmark():
    size = 10000
    device = "cuda" if torch.cuda.is_available() else "cpu"
    A = torch.rand(size, size, device=device)
    B = torch.rand(size, size, device=device)
    
    start_time = time.time()
    C = torch.matmul(A, B)
    torch.cuda.synchronize()  # Wait for GPU to finish
    end_time = time.time()
    
    print(f"GPU Benchmark: {end_time - start_time} seconds")

gpu_benchmark()