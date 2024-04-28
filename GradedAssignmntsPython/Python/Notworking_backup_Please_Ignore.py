import os
import shutil
import sys
from datetime import datetime

def backup_files(source_dir, dest_dir):
    # Check if source directory exists
    if not os.path.exists(source_dir):
        print(f"Error: Source directory '{source_dir}' does not exist.")
        return
    
    # Check if destination directory exists, create if not
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    
    # Iterate through files in source directory
    for filename in os.listdir(source_dir):
        source_file = os.path.join(source_dir, filename)
        dest_file = os.path.join(dest_dir, filename)
        
        # Check if destination file already exists
        if os.path.exists(dest_file):
            # Append timestamp to filename for uniqueness
            timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
            dest_file = os.path.join(dest_dir, f"{os.path.splitext(filename)[0]}_{timestamp}{os.path.splitext(filename)[1]}")
        
        # Copy file from source to destination
        try:
            shutil.copy2(source_file, dest_file)
            print(f"Copied '{source_file}' to '{dest_file}'")
        except Exception as e:
            print(f"Error: Failed to copy '{source_file}' to '{dest_file}': {e}")

if __name__ == "__main__":
    # Check if command-line arguments are provided
    if len(sys.argv) != 3:
        
        sys.exit(1)
    
    # Get source and destination directories from command-line arguments
    source_dir = sys.argv[1]
    dest_dir = sys.argv[2]
    
    # Call backup_files function with provided directories
    backup_files(source_dir, dest_dir)
