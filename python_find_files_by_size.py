import os
import sys

def find_files_by_size(directory, min_size, max_size):
    found_files = []
    try:
        # Walk through the directory and find files within the size range
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                file_size = os.path.getsize(file_path)
                if min_size <= file_size <= max_size:
                    found_files.append(file_path)
        return found_files
    except Exception as e:
        print(f"Error locating files: {e}")
        return []

if __name__ == "__main__":
    # Provide directory path, minimum size, and maximum size as command-line arguments
    if len(sys.argv) != 4:
        print("Usage: python script.py <directory> <min_size> <max_size>")
        sys.exit(1)
    
    directory = sys.argv[1]
    min_size = int(sys.argv[2])
    max_size = int(sys.argv[3])

    found_files = find_files_by_size(directory, min_size, max_size)
    if found_files:
        print("Found files within the size range:")
        for file_path in found_files:
            print(file_path)
    else:
        print("No files found within the specified size range.")
