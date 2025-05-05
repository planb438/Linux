import subprocess       
# #       # Function to list installed packages
# #       # This script lists installed packages on a Linux system using the dpkg command.      

def list_installed_packages():  
    """
    List installed packages on a Linux system using dpkg.
    Returns:
        list: A list of installed package names.
    """             
    try:
        # Check if dpkg is available
        subprocess.run(['dpkg', '--version'], check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError:
        print("dpkg command not found. This script is intended for Debian-based systems.")
        return []
    except FileNotFoundError:
        print("dpkg command not found. This script is intended for Debian-based systems.")
        return []                   
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
    except Exception as e:
        print("An error occurred:", e)
        return []
    # Note: This script lists installed packages on a Linux system using the dpkg command.
    # It uses the subprocess module to run system commands.
    # The script is useful for system administrators to audit installed software.
    # It can be run as a standalone program or imported as a module.            
    
if __name__ == "__main__":
    installed_packages = list_installed_packages()
    print("Installed Packages:")
    for package in installed_packages:
        print(package)




