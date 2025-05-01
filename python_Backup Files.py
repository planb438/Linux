import shutil
import os
import datetime
# Function to create a backup of files
def backup_files(source_dir, backup_dir):
    # Get the current date and time
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y%m%d_%H%M%S")
    
    # Create a new backup directory with the timestamp
    backup_dir_with_timestamp = os.path.join(backup_dir, f"backup_{timestamp}")
    os.makedirs(backup_dir_with_timestamp, exist_ok=True)
    
    # Copy files from source to backup directory
    for item in os.listdir(source_dir):
        source_item = os.path.join(source_dir, item)
        dest_item = os.path.join(backup_dir_with_timestamp, item)
        if os.path.isdir(source_item):
            shutil.copytree(source_item, dest_item)
        else:
            shutil.copy2(source_item, dest_item)
# Example usage

if __name__ == "__main__":
    # Specify source and destination directories
    source_dir = '/path/to/source'
    backup_dir = '/path/to/backup'

    # Create a backup of files
    backup_files(source_dir, backup_dir)
    print(f"Backup completed successfully to {backup_dir}")
# Note: Replace '/path/to/source' and '/path/to/backup' with actual paths
# This script creates a backup of files from a source directory to a backup directory.
# It creates a new backup directory with a timestamp to avoid overwriting previous backups.
# It uses the shutil module to copy files and directories.
# The os module is used to handle file paths and directory creation.
# The datetime module is used to generate a timestamp for the backup directory name.
# The script can be run as a standalone program or imported as a module.
# The backup_files function takes two arguments: source_dir and backup_dir.
# It creates a new directory in the backup location with the current date and time.
# It then copies all files and directories from the source directory to the new backup directory.
# The script uses the os.makedirs function to create the backup directory if it doesn't exist.
# The shutil.copytree function is used to copy entire directories, while shutil.copy2 is used for files.
# The script prints a success message after the backup is completed.
# This script is useful for creating backups of important files and directories.
# It can be scheduled to run at regular intervals using a task scheduler or cron job.
# This script is a simple and effective way to ensure that important files are backed up regularly.
# It can be modified to include additional features such as logging, error handling, and email notifications.
# The script can be extended to include options for incremental backups, compression, and encryption.
# It can also be integrated with cloud storage services for remote backups.
# The script can be customized to suit specific backup requirements and workflows.
# The script is written in Python and can be run on any platform that supports Python.
# The script is compatible with Python 3.x and uses standard libraries.
# The script is easy to understand and modify, making it suitable for both beginners and experienced programmers.
# The script can be used as a starting point for building more complex backup solutions.            
