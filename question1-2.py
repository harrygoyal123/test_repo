# Que1  Get System Details like Uptime, CPU Utilization, Disk Usage , Memory Utilization

print('Harry Goyal')                             # print name
# code start
import psutil                                    # import psutil module to get all info about System Details
import platform                                  # import platform module to get system related info
import time                                      # include time module to calculate up time
from datetime import datetime                    # import datetime module to work with date as date objects
def get_size(bytes, suffix="B"):                 # Declare function for units
    factor = 1024                                # declare a variable with 1024 value
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:                       # if condition
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor
def seconds_elapsed():                           # Declare function to get total up time
    return time.time() - psutil.boot_time()

#system info
print("^"*22, "System Information", "^"*22)
sysname = platform.uname()                       # Return a named tuple containing system, node, release, version, machine as attributes
print(f"System: {sysname.system}, Name: {sysname.node}, Release: {sysname.release}, Version: {sysname.version}, Machine: {sysname.machine}")

#Up Time
print("^"*28, "Up time", "^"*28)
boot_time_timestamp = psutil.boot_time()
print(f"Up time:- {seconds_elapsed()} seconds")    # print output of uptime from function
bt = datetime.fromtimestamp(boot_time_timestamp)
print(f"from date and time: {bt.year}/{bt.month}/{bt.day} {bt.hour}:{bt.minute}:{bt.second}")   # print date and time in detail of last boot up

#CPU Utilization
print("^"*24, "CPU Utilization", "^"*24)
print(f"Total CPU Utilization: {psutil.cpu_percent()}%")  # Return CPU Utilization

#Disk Usage
print("^"*25, "Disk Usage", "^"*25)
print(psutil.disk_usage('/'))                       # Return disk usage statistics about the partition including total,free & used space

#Memory Utilization
print("^"*22, "Memory Utilization", "^"*21)
svmem = psutil.virtual_memory()                     # This function gives total memory usage in bytes
print(f"Total: {get_size(svmem.total)}")            # total parameter for total physical memory
print(f"Available: {get_size(svmem.available)}")    # Available parameter for memory that given instantly to processes
print(f"Used: {get_size(svmem.used)}")              # used parameter for the memory used
print(f"Memory Utilization Percentage: {svmem.percent}%")  # to get total memory utilization percentage
# code end