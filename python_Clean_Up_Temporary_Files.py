import os
import glob

# Specify temporary file directory
temp_dir = '/tmp'

# Clean up temporary files older than 7 days
for file in glob.glob(os.path.join(temp_dir, '*')):
    if os.stat(file).st_mtime < (time.time() - 7 * 86400):
        os.remove(file)
