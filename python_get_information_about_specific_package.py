import subprocess
import sys

def get_package_information(package_name):
    try:
        # Run apt-cache command to get package information
        result = subprocess.run(['apt-cache', 'show', package_name], capture_output=True, text=True, check=True)
        package_info = result.stdout

        return package_info
    except subprocess.CalledProcessError as e:
        print(f"Failed to get information for package '{package_name}': {e}")
        return ""

if __name__ == "__main__":
    # Provide the package name as a command-line argument
    if len(sys.argv) != 2:
        print("Usage: python script.py <package_name>")
        sys.exit(1)
    
    package_name = sys.argv[1]
    package_info = get_package_information(package_name)
    
    if package_info:
        print(package_info)
