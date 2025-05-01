import os
# Function to retrieve command history from the user's shell
# This script retrieves the command history from the user's shell.
# It reads the command history file and prints the commands executed by the user.
# The script is useful for auditing and monitoring user activity on the system.
# The script can be run as a standalone program or imported as a module.        
# The script is written in Python and can be run on any platform that supports Python.
# The script is compatible with Python 3.x and uses standard libraries.
# The script is easy to understand and modify, making it suitable for both beginners and experienced programmers.
# The script can be used as a starting point for building more complex command history analysis tools.
# The script can be integrated with other tools and frameworks for enhanced functionality.
# The script can be scheduled to run at regular intervals using a task scheduler or cron job.
# The script can be modified to include options for filtering, sorting, and exporting results.
# The script can be customized to suit specific command history analysis requirements and workflows.
# The script can be used to monitor user activity, identify security incidents, or analyze usage patterns.          

def get_command_history():  
    """
    Retrieve command history from the user's shell.
    Returns:
        list: A list of commands executed by the user.
    """
    import os
    import subprocess
    import sys
    import platform
    import getpass
    import pwd
    try:
        # Get  the user's home directory
        home_dir = os.path.expanduser("~")
        # Check the operating system
        if platform.system() == "Windows":
            # For Windows, use the PowerShell command history
            history_file = os.path.join(home_dir, "AppData", "Roaming", "Microsoft", "Windows", "PowerShell", "PSReadLine", "ConsoleHost_history.txt")
        else:
            # For Linux and macOS, use the bash history file
            history_file = os.path.join(home_dir, ".bash_history")
        # Check if the history file exists
        if not os.path.exists(history_file):
            print(f"History file not found: {history_file}")
            return []
        # Check if the user has permission to read the history file
        if not os.access(history_file, os.R_OK):
            print(f"Permission denied: {history_file}")
            return []
        # Get the current user
        current_user = getpass.getuser()
        # Get the user's home directory
        user_info = pwd.getpwnam(current_user)
        home_dir = user_info.pw_dir
        # Check if the history file exists
        if not os.path.exists(history_file):
            print(f"History file not found: {history_file}")
            return []
        # Check if the user has permission to read the history file
        if not os.access(history_file, os.R_OK):
            print(f"Permission denied: {history_file}")
            return []
        # Check if the history file is empty
        if os.path.getsize(history_file) == 0:
            print(f"History file is empty: {history_file}")
            return []
        # Check if the history file is a regular file
        if not os.path.isfile(history_file):
            print(f"History file is not a regular file: {history_file}")
            return []
        # Check if the history file is readable
        if not os.access(history_file, os.R_OK):
            print(f"History file is not readable: {history_file}")
            return []
        # Check if the history file is writable
        if not os.access(history_file, os.W_OK):
            print(f"History file is not writable: {history_file}")
            return []           
        # Path to the command history file  
        history_file = os.path.join(home_dir, ".bash_history")  
        
        # Read the command history filea
        with open(history_file, "r") as file:
            command_history = file.readlines()
        # Remove empty lines and strip whitespace
        command_history = [line.strip() for line in command_history if line.strip()]
        # Check if the command history is empty
        if not command_history:
            print("Command history is empty.")
            return []
        # Check if the command history is a list
        if not isinstance(command_history, list):
            print("Command history is not a list.")
            return []
        # Check if the command history is a string
        if isinstance(command_history, str):
            print("Command history is a string.")
            return []
        # Check if the command history is a dictionary
        if isinstance(command_history, dict):
            print("Command history is a dictionary.")
            return []
        # Check if the command history is a set
        if isinstance(command_history, set):
            print("Command history is a set.")
            return []       
        return command_history
    except Exception as e:
            print(f"Failed to retrieve command history: {e}")
            return []
    # Note: This script retrieves the command history from the user's shell.
    # It reads the command history file and prints the commands executed by the user.
    # The script is useful for auditing and monitoring user activity on the system.
    # The script can be run as a standalone program or imported as a module.
    # The script is written in Python and can be run on any platform that supports Python.
if __name__ == "__main__":
    command_history = get_command_history()
    
    if command_history:
        print("Command History:")
        for index, command in enumerate(command_history, start=1):
            print(f"{index}. {command.strip()}")
    else:
        print("No command history found.")
