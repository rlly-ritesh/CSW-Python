import numpy as np
import matplotlib.pyplot as plt
# Create data
x = np.linspace(0, 2*np.pi, 100)
y1 = np.sin(x)
y2 = np.cos(x)
y3 = np.sin(x) + np.cos(x)
# Plot multiple lines
plt.plot(x, y1, label='sin(x)', color='blue', linewidth=2)
plt.plot(x, y2, label='cos(x)', color='red', linewidth=2)
plt.plot(x, y3, label='sin(x) + cos(x)', color='green',
linewidth=2, linestyle='--')
plt.xlabel('Angle (radians)')
plt.ylabel('Value')
plt.title('Multiple Trigonometric Functions')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()