import subprocess

def list_installed_packages():
    try:
        # Run dpkg command to list installed packages
        result = subprocess.run(['dpkg', '--get-selections'], capture_output=True, text=True, check=True)
        installed_packages = result.stdout.split('\n')

        # Filter out empty lines and extract package names
        package_names = [line.split('\t')[0] for line in installed_packages if line.strip()]

        return package_names
    except subprocess.CalledProcessError as e:
        print("Failed to list installed packages:", e)
        return []

if __name__ == "__main__":
    installed_packages = list_installed_packages()
    print("Installed Packages:")
    for package in installed_packages:
        print(package)
