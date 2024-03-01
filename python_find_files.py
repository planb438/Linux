import os
import sys

def find_files(directory, pattern):
    found_files = []
    try:
        # Walk through the directory and find files matching the pattern
        for root, dirs, files in os.walk(directory):
            for file in files:
                if pattern in file:
                    found_files.append(os.path.join(root, file))
        return found_files
    except Exception as e:
        print(f"Error finding files: {e}")
        return []

if __name__ == "__main__":
    # Provide directory path and filename pattern as command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python script.py <directory> <pattern>")
        sys.exit(1)
    
    directory = sys.argv[1]
    pattern = sys.argv[2]

    found_files = find_files(directory, pattern)
    if found_files:
        print(f"Found files matching '{pattern}':")
        for file_path in found_files:
            print(file_path)
    else:
        print(f"No files found matching '{pattern}'.")
