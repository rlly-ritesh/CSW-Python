import numpy as np

# Define angles in radians
angles = np.array([0, np.pi/6, np.pi/4, np.pi/3, np.pi/2])

# Compute trigonometric values
sin_values = np.sin(angles)
cos_values = np.cos(angles)
tan_values = np.tan(angles)

# Display results
print("Angles (radians):", angles)
print("Sine values:      ", np.round(sin_values, 4))
print("Cosine values:    ", np.round(cos_values, 4))
print("Tangent values:   ", np.round(tan_values, 4))
