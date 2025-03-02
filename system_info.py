import psutil
import platform
import GPUtil
import json
from typing import Dict, Any

def get_system_info() -> Dict[str, Any]:
    # CPU 信息
    cpu_info = {
        "cpu_model": platform.processor(),
        "cpu_cores": psutil.cpu_count(),
        "cpu_usage": psutil.cpu_percent(interval=1),
    }
    
    # 内存信息
    memory = psutil.virtual_memory()
    memory_info = {
        "total_memory": round(memory.total / (1024**3), 2),  # GB
        "memory_usage": memory.percent,
        "available_memory": round(memory.available / (1024**3), 2)  # GB
    }
    
    # GPU 信息
    gpu_info = []
    try:
        gpus = GPUtil.getGPUs()
        for gpu in gpus:
            gpu_info.append({
                "gpu_model": gpu.name,
                "gpu_memory_total": gpu.memoryTotal,  # MB
                "gpu_memory_used": gpu.memoryUsed,    # MB
                "gpu_memory_usage": round((gpu.memoryUsed / gpu.memoryTotal) * 100, 2),
                "gpu_temperature": gpu.temperature
            })
    except Exception:
        gpu_info = None
    
    # 系统信息
    system_info = {
        "os": platform.system(),
        "os_version": platform.version(),
        "hostname": platform.node(),
        "architecture": platform.machine(),
    }
    
    # 磁盘信息
    disk = psutil.disk_usage('/')
    disk_info = {
        "total_disk": round(disk.total / (1024**3), 2),  # GB
        "used_disk": round(disk.used / (1024**3), 2),    # GB
        "disk_usage": disk.percent
    }
    
    # 整合所有信息
    all_info = {
        "cpu": cpu_info,
        "memory": memory_info,
        "gpu": gpu_info,
        "system": system_info,
        "disk": disk_info
    }
    
    return all_info

if __name__ == "__main__":
    print(json.dumps(get_system_info(), indent=2))