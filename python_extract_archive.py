import subprocess
import sys

def extract_archive(archive_name, destination='.'):
    try:
        # Construct the tar command
        tar_command = ['tar', '-xzvf', archive_name, '-C', destination]
        
        # Run the tar command
        subprocess.run(tar_command, check=True)
        print(f"Archive '{archive_name}' extracted successfully to '{destination}'.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to extract archive: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Provide archive name and optional destination directory as command-line arguments
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python script.py <archive_name> [destination]")
        sys.exit(1)
    
    archive_name = sys.argv[1]
    destination = sys.argv[2] if len(sys.argv) == 3 else '.'

    extract_archive(archive_name, destination)
