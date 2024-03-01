import subprocess
import sys

def create_archive(archive_name, files):
    try:
        # Construct the tar command
        tar_command = ['tar', '-czvf', archive_name] + files
        
        # Run the tar command
        subprocess.run(tar_command, check=True)
        print(f"Archive '{archive_name}' created successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to create archive: {e}")
        sys.exit(1)

if __name__ == "__main__":
    # Provide archive name and list of files/directories to include in the archive as command-line arguments
    if len(sys.argv) < 3:
        print("Usage: python script.py <archive_name> <file1> <file2> ...")
        sys.exit(1)
    
    archive_name = sys.argv[1]
    files = sys.argv[2:]

    create_archive(archive_name, files)
