import numpy as np
# Create structured array
dtype = [('name', 'U20'), ('score', 'f8')]
students = np.array([
('Alice', 95.5),
('Bob', 87.3),
('Charlie', 92.1)
], dtype=dtype)
# Save structured array
np.save('students.npy', students)
# Load and display
loaded_students = np.load('students.npy')
print("Student Records:")
for student in loaded_students:
    print(f" {student['name']}: {student['score']:.1f}")
# Compressed save (.npz with compression)
large_array = np.random.rand(1000, 1000)
np.savez_compressed('large_data.npz', data=large_array)
print("\nCompressed data saved")