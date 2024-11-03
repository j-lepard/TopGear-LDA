import torch

# Check if CUDA is available
cuda_available = torch.cuda.is_available()
print(f"CUDA available: {cuda_available}")



if cuda_available:
    # Get the GPU name
    print(f"GPU name: {torch.cuda.get_device_name(0)}")

    # Test GPU by moving a tensor to the GPU and performing a simple operation
    tensor = torch.rand(3, 3)
    tensor_gpu = tensor.to('cuda')  # Move tensor to GPU
    print("Tensor on GPU:", tensor_gpu)

    # Perform a simple operation on the GPU
    result = tensor_gpu * 2
    print("Result after operation on GPU:", result)
