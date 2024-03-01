import subprocess
import sys

def reconfigure_package(package_name):
    try:
        # Run dpkg-reconfigure command
        subprocess.run(['dpkg-reconfigure', package_name], check=True)
        print(f"Package '{package_name}' reconfigured successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to reconfigure package '{package_name}': {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Provide the package name as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <package_name>")
        sys.exit(1)
    
    package_name = sys.argv[1]
    reconfigure_package(package_name)
