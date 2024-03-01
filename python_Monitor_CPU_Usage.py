import psutil

# Get CPU usage statistics
cpu_usage = psutil.cpu_percent(interval=1, percpu=True)

# Print CPU usage information
print("CPU Usage:")
for i, usage in enumerate(cpu_usage):
    print(f"CPU {i + 1}: {usage}%")
