import numpy as np
import matplotlib.pyplot as plt
# Create circle using parametric equations
theta = np.linspace(0, 2*np.pi, 100)
radius = 5
x = radius * np.cos(theta)
y = radius * np.sin(theta)
# Plot without aspect ratio correction
plt.figure(figsize=(12, 5))
plt.subplot(1, 2, 1)
plt.plot(x, y, linewidth=2)
plt.title('Without Aspect Ratio (Ellipse)')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
# Plot with aspect ratio correction
plt.subplot(1, 2, 2)
plt.plot(x, y, linewidth=2)
plt.axis('equal') # Set equal aspect ratio
plt.title('With Aspect Ratio (Circle)')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.tight_layout()
plt.show()