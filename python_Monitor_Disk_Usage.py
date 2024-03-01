import psutil

# Get disk usage statistics
disk_usage = psutil.disk_usage('/')

# Print disk usage information
print("Disk Usage:")
print("Total:", disk_usage.total)
print("Used:", disk_usage.used)
print("Free:", disk_usage.free)
print("Percentage:", disk_usage.percent)
