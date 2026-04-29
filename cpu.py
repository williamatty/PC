import psutil
import platform
import GPUtil

def get_system_status():
    print(f"--- 🖥️ 系统硬件实时监控 ---")
    print(f"操作系统: {platform.system()} {platform.release()}")
    print(f"CPU 物理核心: {psutil.cpu_count(logical=False)}")
    
    # --- 内存监控 ---
    mem = psutil.virtual_memory()
    total_gb = round(mem.total / (1024**3), 2)
    used_gb = round(mem.used / (1024**3), 2)
    print(f"内存占用: {mem.percent}% ({used_gb}GB / {total_gb}GB)")

    # --- 磁盘监控 ---
    disk = psutil.disk_usage('/')
    print(f"磁盘使用率: {disk.percent}%")

    # --- 显存监控 (GPU) ---
    try:
        gpus = GPUtil.getGPUs()
        if not gpus:
            print("显存占用: 未检测到兼容的 NVIDIA 显卡")
        for gpu in gpus:
            print(f"显卡型号: {gpu.name}")
            print(f"显存占用: {gpu.memoryUtil*100:.1f}% ({round(gpu.memoryUsed/1024, 2)}GB / {round(gpu.memoryTotal/1024, 2)}GB)")
    except Exception as e:
        print(f"显存占用: 获取失败 (可能未安装驱动或非 NVIDIA 显卡)")

if __name__ == "__main__":
    get_system_status()
