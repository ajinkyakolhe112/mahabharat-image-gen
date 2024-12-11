import torch
torch.cuda.mem_get_info()

def get_gpu_memory():
    """Get GPU memory stats in GB"""
    gpu_stats    = torch.cuda.get_device_properties(0)
    total_memory = round(gpu_stats.total_memory / 1024**3, 2)

    used_memory  = round(torch.cuda.memory_allocated() / 1024**3, 2)
    
    return f"GPU = {gpu_stats.name}. Memory: {used_memory}GB / {total_memory}GB"
get_gpu_memory()