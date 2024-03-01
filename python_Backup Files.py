import shutil

# Specify source and destination directories
source_dir = '/path/to/source'
backup_dir = '/path/to/backup'

# Copy files from source to backup directory
shutil.copytree(source_dir, backup_dir)
