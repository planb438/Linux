import subprocess

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
    ]

    for command in commands:
        try:
            # Run the command and capture output
            result = subprocess.run(command.split(), capture_output=True, text=True, check=True)
            output = result.stdout

            # Print command output
            print(f"Command: {command}")
            print(output)
            print("=" * 80)
        except subprocess.CalledProcessError as e:
            print(f"Failed to execute command '{command}': {e}")

if __name__ == "__main__":
    execute_commands()
