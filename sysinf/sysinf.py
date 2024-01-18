import psutil
import platform
import cpuinfo
import GPUtil
import os


class SysInf:

    def __init__(self):
        self.psutil = psutil
        self.platform = platform

# CPU
    def cpuload(self):
        load = psutil.cpu_percent()
        return f"Current load: {load}%"

    def cpubrand(self):
        brand = cpuinfo.get_cpu_info()["brand_raw"]
        return brand

    def cpucores(self):
        cores =  [f"Core #{core}: {perc}%{os.linesep}"
                for core, perc in enumerate(psutil.cpu_percent(percpu=True, interval=1))]
        return "".join(cores)

    def corecount(self):
        corecount = psutil.cpu_count()
        return f"{corecount} Cores"

    def cpuspeeds(self):
        cpu_max = cpuinfo.get_cpu_info()["hz_advertised_friendly"]
        cpu_actual = cpuinfo.get_cpu_info()["hz_actual_friendly"]
        return f"CPU speed: {cpu_actual} ({cpu_max})"

# memory
    def memtotal(self):
        mem_total = round(psutil.virtual_memory().total / (1024. ** 3))
        return f"Installed memory: {mem_total} GB"

    def memused(self):
        mem_used = round(psutil.virtual_memory().used / (1024. ** 3))
        return f"Used memory: {mem_used} GB"

    def memavail(self):
        mem_avail = round(psutil.virtual_memory().available / (1024. ** 3))
        return f"Available memory: {mem_avail} GB"

# drives
    def drivelist(self):
        drives = psutil.disk_partitions()
        drive_info_list = []
        for drive in drives:
            try:
                drive_usage = psutil.disk_usage(drive.mountpoint)
            except PermissionError:
                continue
            drive_list = f"{drive.mountpoint} ({drive.fstype})"
            drive_total = drive_usage.total // (1024 ** 3)
            drive_used = drive_usage.used // (1024 ** 3)
            drive_free = drive_usage.free // (1024 ** 3)
            drive_info = (f"{drive_list}\nTotal Size: {drive_total} GB"
                          f"\nUsed: {drive_used} GB\nFree: {drive_free} GB")
            drive_info_list.append(drive_info)
            return "".join(drive_info_list)

# system
    def sysinfo(self):
        sys = platform.uname()
        sysinfo = f"Device Name: {sys.node}\nOS: {sys.system} {sys.release}\nVersion: {sys.version}"
        return sysinfo

# GPU

    def gpulist(self):
        gpu_list = GPUtil.getGPUs()
        gpus = []
        if gpu_list:
            for gpu in gpu_list:
                gpu_total = gpu.memoryTotal // 1024
                gpu_used = gpu.memoryUsed // 1024
                gpu_free = gpu.memoryFree // 1024
                gpu_name = f"{gpu.name} {gpu_total:.0f} GB"
                gpu_stats = (f"Current Load: {gpu.load * 100:.0f}%"
                             f"\nCurrent Temp: {gpu.temperature:.0f}°C"
                             f"\nUsed: {gpu_used:.0f} GB\n"
                             f"Free: {gpu_free:.0f} GB")
                gpu_info = f"{gpu_name}\n{gpu_stats}\n"
                gpus.append(gpu_info)
        else:
            print("ERROR: No GPU detected")
        listgpus = "\n\n".join(gpus)
        return listgpus
