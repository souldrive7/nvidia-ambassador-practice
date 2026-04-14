import torch

print("PyTorch version:", torch.__version__)
print("CUDA available:", torch.cuda.is_available())
print("GPU count:", torch.cuda.device_count())

if torch.cuda.is_available():
    print("GPU name:", torch.cuda.get_device_name(0))
    x = torch.tensor([1.0, 2.0, 3.0], device="cuda")
    y = x * 2
    print("Tensor on GPU:", y)
