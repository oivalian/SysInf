# **SysInf**

SysInf is a small package that simplfies system information into pre-defined strings.

___

### Dependancies

SysInfo is dependant on the following libraries:

3) ```psutil```
4) ```py-cpuinfo```
5) ```GPUtil```
   
___

### Documentation

Getting Started:

```
# import module:
import sysinf

# Assign the function to a variable: 
sysinf = sysinf.SysInf()
```


**-- CPU Functions --**

Get CPU load with percentage as float
```
sysinf.cpuload()

# As example, would output as:

Current load: 5.3%
```

Get CPU model
```
sysinf.cpubrand()

# As example, would output as:

AMD Ryzen 9 5900X 12-Core Processor
``````

Get total cores
```
sysinf.coretotal()

# As example, would output as:

12 Cores
```

Get core load breakdown as float
```
sysinf.cpucores()

# As example, would output as:

Core #0: 3.0%
Core #1: 0.0%
Core #2: 1.2%
Core #4: 0.0%
(etc...)
```

Get max and actual core speed as float
```
sysinf.cpuspeeds()

# As example, would output as:

4.1760 GHz (4.1750 GHz)
```


**-- Memory Functions --**

Get total physical memory
```
sysinfo.memtotal()

# As example, will output as:

Installed memory: 32 GB
```

Get total used memory
```
sysinfo.memused()

# As example, would output as:

Used: 7 GB
```

Get total available memory
```
sysinf.memavail()

# As example, would output as:

Available memory: 25 GB
```


**-- Drive Function --**

Get list of ALL connected drives and breakdown
```
sysinf.drivelist()

# As example, would output as:

C:/ (NTFS)
Total Size: 250 GB
Used: 120 GB
Free: 108

D:/ (FAT32)
(etc..)
```


**-- GPU Function --**
>[!WARNING]
> The GPU functionality is only suitable for Nvidia GPUs. Check the GPUtil documentation for more information

Get GPUs and breakdown
```
sysinf.listgpus()

# As example, would output as:

Nvidia GeForce RTX 2070 SUPER 8GB
Current Load: 11%
Current Temp: 47°C
Used: 1GB
Free: 5GB

(etc...)
```

>[!NOTE]
>No GPU will display a 'No GPU Detected' prompt


**-- System Function --**

Get System Information
```
sysinf.sysinfo()

As example, would output as:

"Device Name: My Device
OS: Windows 11
Version: 10.0.22621
```
