# Writing to a binary file
def write_binary_file():
    # Create some binary data
    data = b'\x48\x65\x6C\x6C\x6F'  # "Hello" in bytes
    file = open('sample.bin', 'wb')
    file.write(data)
    file.close()
    print("Binary file created successfully!")

# Reading from a binary file
def read_binary_file():
    file = open('sample.bin', 'rb')
    data = file.read()
    file.close()
    return data

# Execute the functions
write_binary_file()
binary_data = read_binary_file()
print(f"Binary data: {binary_data}")
print(f"Decoded: {binary_data.decode('utf-8')}")