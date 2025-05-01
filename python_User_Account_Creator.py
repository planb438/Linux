import subprocess       
#       # Function to create a new user
#       # This script creates a new user on a Linux system using the useradd command.
#       # It uses the subprocess module to run system commands.
#       # The script is useful for system administrators to automate user management tasks.
#       # It can be used to create user accounts for new employees, contractors, or temporary users.
#       # The script can be run as a standalone program or imported as a module.
#       # The script is written in Python and can be run on any platform that supports Python.

def create_user(username, password):
    # Check if the username is valid
    if not username.isalnum():
        raise ValueError("Username must be alphanumeric.")
    # Check if the password is strong enough
    if len(password) < 8:
        raise ValueError("Password must be at least 8 characters long.")                
    # Create the user                        
    subprocess.run(['useradd', '-m', username])
    # Set the password for the user
    # Note: The --stdin option is used to read the password from standard input
    # This may not be available on all systems. If not, use a different method to set the password.
    # For example, use chpasswd or expect to automate password entry.
    subprocess.run(['passwd', '--stdin', username], input=password.encode())
    print(f"User '{username}' created successfully.")
    # Note: This script requires root privileges to create users.
    # It can be run with sudo or as a root user.
    # The script uses the subprocess module to run system commands.
    # The subprocess.run function is used to execute commands and capture output.

if __name__ == "__main__":
    username = "newuser"
    password = "password"
    create_user(username, password)
