import os

# Specify the directory you want to list
directory_Path = "D:\Python\Python BY CodeWithHarry"

# Get the list of files and directories
contents = os.listdir(directory_Path)

# Print the contents
print("Contents of the directory:")
for item in contents:
    print(item)
