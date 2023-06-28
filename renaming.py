import argparse
import os
import shutil

# Create the parser to determine root directory from argument in the command line
parser = argparse.ArgumentParser(description="Rename files in a directory")
parser.add_argument("--root-path", type=str, required=True, help="The root directory")
args = parser.parse_args()
root_dir = args.root_path

# Get the name of the root directory
root_name = os.path.basename(root_dir)

# Walk through root directory
for dir_path, dir_names, file_names in os.walk(root_dir):
    # Iterate over each file in directory and subdirectories
    for file_name in file_names:
        # Check if the file is a .png file
        if file_name.endswith(".png"):
            # Split the file name into parts
            parts = file_name.split("_")
            # Check if the file name has the correct format
            if len(parts) >= 3:
                # Construct the new file name
                new_file_name = (
                    root_name
                    + "_"
                    + dir_path.split(root_name + os.sep, 1)[1].replace(os.sep, "_")
                    + "_"
                    + "_".join(parts[2:])
                )
                # Create the full file path for the new file name
                new_file_path = os.path.join(dir_path, new_file_name)
                # Create the full file path for the old file name
                old_file_path = os.path.join(dir_path, file_name)
                # Rename the file
                shutil.move(old_file_path, new_file_path)

print("Done!")
