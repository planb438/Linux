import os

def get_command_history():
    try:
        # Get the user's home directory
        home_dir = os.path.expanduser("~")

        # Path to the command history file
        history_file = os.path.join(home_dir, ".bash_history")

        # Read the command history file
        with open(history_file, "r") as file:
            command_history = file.readlines()

        return command_history
    except Exception as e:
        print(f"Failed to retrieve command history: {e}")
        return []

if __name__ == "__main__":
    command_history = get_command_history()
    
    if command_history:
        print("Command History:")
        for index, command in enumerate(command_history, start=1):
            print(f"{index}. {command.strip()}")
    else:
        print("No command history found.")
