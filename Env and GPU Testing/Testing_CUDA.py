import torch
import os
# os.system('ffmpeg -version')


print(torch.cuda.is_available())  # This should return True if CUDA is available
print(torch.version.cuda)  # This will print the version of CUDA being used by PyTorch