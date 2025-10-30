import numpy as np

# Load data from a .npy file (assuming 'loaded_data' was previously defined)
# Uncomment the line below if 'data.npy' exists and you want to load it
# loaded_data = np.load('data.npy')
# print("\nLoaded data from 'data.npy':")
# print(loaded_data)

# Save multiple arrays to a .npz file
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
array3 = np.array([[1, 2], [3, 4]])

np.savez('multiple_arrays.npz', first=array1, second=array2, third=array3)
print("\nMultiple arrays saved to 'multiple_arrays.npz'")

# Load arrays from the .npz file
loaded_npz = np.load('multiple_arrays.npz')

print("\nFirst array:", loaded_npz['first'])
print("Second array:", loaded_npz['second'])
print("Third array:")
print(loaded_npz['third'])