import os
import sys
import time

def find_files_by_modification_time(directory, seconds):
    try:
        # Get the current time
        current_time = time.time()

        # Calculate the modification time threshold
        modification_threshold = current_time - seconds

        # Walk through the directory and find files modified within the threshold
        found_files = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                file_path = os.path.join(root, file)
                modification_time = os.path.getmtime(file_path)
                if modification_time >= modification_threshold:
                    found_files.append(file_path)

        return found_files
    except Exception as e:
        print(f"Error locating files: {e}")
        return []

if __name__ == "__main__":
    # Provide directory path and time threshold in seconds as command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python script.py <directory> <seconds>")
        sys.exit(1)
    
    directory = sys.argv[1]
    seconds = int(sys.argv[2])

    found_files = find_files_by_modification_time(directory, seconds)
    if found_files:
        print("Found files modified within the last", seconds, "seconds:")
        for file_path in found_files:
            print(file_path)
    else:
        print("No files found.")
