import numpy as np
import matplotlib.pyplot as plt

# Generate data
x = np.linspace(0, 2 * np.pi, 100)
y = np.sin(x)

# Create a customized line plot
plt.figure(figsize=(10, 6))
plt.plot(
    x, y,
    color='blue',
    linewidth=2,
    linestyle='-',
    marker='o',
    markersize=3,
    label='sin(x)'
)

# Add labels and title
plt.xlabel('Angle (radians)', fontsize=12)
plt.ylabel('Amplitude', fontsize=12)
plt.title('Customized Sine Wave', fontsize=14, fontweight='bold')

# Add legend and grid
plt.legend()
plt.grid(True, alpha=0.3)

# Display the plot
plt.show()