import psutil

# Get network interface statistics
net_io_counters = psutil.net_io_counters(pernic=True)

# Print network interface traffic information
print("Network Interface Traffic:")
for interface, stats in net_io_counters.items():
    print(f"Interface: {interface}")
    print("Bytes Sent:", stats.bytes_sent)
    print("Bytes Received:", stats.bytes_recv)
    print("Packets Sent:", stats.packets_sent)
    print("Packets Received:", stats.packets_recv)
