import os

# Path of the directory
path = "/"

# List all files and folders
contents = os.listdir(path)

# Print each item
for item in contents:
    print(item)
