import psutil

# Get memory usage statistics
memory_usage = psutil.virtual_memory()

# Print memory usage information
print("Memory Usage:")
print("Total:", memory_usage.total)
print("Available:", memory_usage.available)
print("Used:", memory_usage.used)
print("Free:", memory_usage.free)
print("Percentage:", memory_usage.percent)
