import subprocess
import sys

def shutdown_system(action):
    try:
        # Run the shutdown command
        subprocess.run(['shutdown', f'-{action}', 'now'], check=True)
        print(f"System {action}ed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to {action} the system: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Provide the action (shutdown or restart) as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <action>")
        sys.exit(1)
    
    action = sys.argv[1].lower()
    if action not in ['shutdown', 'restart']:
        print("Invalid action. Use 'shutdown' or 'restart'.")
        sys.exit(1)
    
    shutdown_system(action)
