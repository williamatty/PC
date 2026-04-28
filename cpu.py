import psutil
import platform

print(f"操作系统: {platform.uname().system}")
print(f"CPU 核心: {psutil.cpu_count(logical=False)}")
print(f"总内存: {round(psutil.virtual_memory().total / (1024**3), 2)} GB")
print(f"磁盘使用率: {psutil.disk_usage('/').percent}%")
