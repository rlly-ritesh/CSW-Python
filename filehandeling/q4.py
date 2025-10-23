import os
def explore_filesystem():
# Get current working directory
    current_dir = os.getcwd()
    print(f"Current directory: {current_dir}")

# List files in current directory
    files = os.listdir('.')
    print(f"Files in current directory: {files}")
# Create a new directory
    new_dir = 'test_directory'
    if not os.path.exists(new_dir):
        os.makedirs(new_dir)
        print(f"Created directory: {new_dir}")
# Create a file in the new directory
file_path = os.path.join('test_file.txt')
with open(file_path, 'w') as f:
    f.write('This is a test file in a subdirectory.')
    print(f"Created file: {file_path}")
# Check if file exists
if os.path.exists(file_path):
    print(f"File {file_path} exists!")
# Get file information
file_size = os.path.getsize(file_path)
print(f"File size: {file_size} bytes")
explore_filesystem()