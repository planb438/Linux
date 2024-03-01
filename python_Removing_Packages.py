import subprocess
import sys

def remove_package(package_name):
    try:
        # Run apt command to remove the package
        subprocess.run(['apt', 'remove', package_name, '-y'], check=True)
        print(f"Package '{package_name}' removed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to remove package '{package_name}': {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Provide the package name as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <package_name>")
        sys.exit(1)
    
    package_name = sys.argv[1]
    remove_package(package_name)
