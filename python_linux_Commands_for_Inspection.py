import subprocess   
# This script executes a series of Linux commands to gather system information.
# It uses the subprocess module to run system commands and capture their output.
# The script is useful for system administrators and developers to inspect system status and performance.
# It can be used to gather information about system resources, network status, and running processes.
# The script can be run as a standalone program or imported as a module.
# The script is written in Python and can be run on any platform that supports Python.
# The script is compatible with Python 3.x and uses standard libraries.
# The script is easy to understand and modify, making it suitable for both beginners and experienced programmers.
# The script can be used as a starting point for building more complex system inspection tools.

def execute_commands(): 
    commands = [    
        "uname -a",             # Print system information
        "df -h",                # Display disk space usage
        "free -h",              # Display memory usage
        "uptime",               # Display system uptime
        "cat /proc/cpuinfo",    # Display CPU information
        "ifconfig",             # Display network interface information
        "netstat -tuln",        # Display listening ports
        "ps aux",               # Display running processes
        "top -b -n 1",          # Display system load
        "lsof -i",              # List open files and network connections
        "who",                  # Display logged-in users
        "last",                 # Display last logged-in users
        "dmesg | tail -n 20",   # Display kernel messages
        "journalctl -xe",       # Display system logs
        "lsblk",                # List block devices        
        "mount",                # Display mounted filesystems
        "crontab -l",           # Display user cron jobs
        "uptime",               # Display system uptime
        "vmstat 1 5",           # Display system performance
        "iostat -x 1 5",        # Display CPU and I/O statistics
        "sar -u 1 5",           # Display CPU usage 
        "sar -r 1 5",           # Display memory usage
        "sar -n DEV 1 5",       # Display network statistics
        "sar -q 1 5",           # Display queue length
        "sar -P ALL 1 5",       # Display CPU usage per processor
        "sar -B 1 5",           # Display paging statistics
        "sar -W 1 5",           # Display swapping statistics
        "sar -d 1 5",           # Display device statistics
        "sar -b 1 5",           # Display I/O statistics
        "sar -n TCP 1 5",       # Display TCP statistics
        "sar -n UDP 1 5",       # Display UDP statistics
        "sar -n EDEV 1 5",      # Display extended device statistics
        "sar -n IP 1 5",        # Display IP statistics
        "sar -n ICMP 1 5",      # Display ICMP statistics
        "sar -n SOCK 1 5",      # Display socket statistics
        "sar -n ALL 1 5",       # Display all network statistics
        "sar -n DEV 1 5",       # Display network device statistics
        "sar -n EDEV 1 5",      # Display extended network device statistics
        "sar -n IP 1 5",        # Display IP statistics
        "sar -n ICMP 1 5",      # Display ICMP statistics
        "sar -n SOCK 1 5",      # Display socket statistics
    ]

    for command in commands:
        # Skip commands that require root privileges
        if command in ["sar -u 1 5", "sar -r 1 5", "sar -n DEV 1 5", "sar -q 1 5", "sar -P ALL 1 5", "sar -B 1 5", "sar -W 1 5", "sar -d 1 5", "sar -b 1 5", "sar -n TCP 1 5", "sar -n UDP 1 5", "sar -n EDEV 1 5", "sar -n IP 1 5", "sar -n ICMP 1 5", "sar -n SOCK 1 5", "sar -n ALL 1 5"]:
            print(f"Skipping command '{command}' that requires root privileges.")
            continue
        # Skip commands that are not available on all systems
        if command in ["sar -u 1 5", "sar -r 1 5", "sar -n DEV 1 5", "sar -q 1 5", "sar -P ALL 1 5", "sar -B 1 5", "sar -W 1 5", "sar -d 1 5", "sar -b 1 5", "sar -n TCP 1 5", "sar -n UDP 1 5", "sar -n EDEV 1 5", "sar -n IP 1 5", "sar -n ICMP 1 5", "sar -n SOCK 1 5", "sar -n ALL 1 5"]:
            print(f"Skipping command '{command}' that is not available on all systems.")
            continue

         # Execute the command
        print(f"Executing command: {command}")
        
        try:
            # Run the command and capture output    


            result = subprocess.run(command.split(), capture_output=True, text=True, check=True)
            output = result.stdout
            # Check for errors


            if result.stderr:
                print(f"Error: {result.stderr}")
                continue
                

            # Print command output
            print(f"Command: {command}")

            print("Output:")
            print(output)
            print("=" * 80)
        except subprocess.CalledProcessError as e:
            print(f"Failed to execute command '{command}': {e}")

if __name__ == "__main__":
    execute_commands()
