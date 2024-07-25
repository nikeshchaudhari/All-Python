
import os

# Specify the directory path
directory_path = '/7th Semester'

# List all files and directories in the specified path
contents = os.listdir(directory_path)

# Print the contents
for item in contents:
    print(item)
