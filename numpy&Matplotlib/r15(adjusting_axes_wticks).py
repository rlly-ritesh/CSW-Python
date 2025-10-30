import numpy as np
import matplotlib.pyplot as plt
# Create data
x = np.linspace(0, 2*np.pi, 100)
y = np.sin(x)
# Create plot
plt.figure(figsize=(10, 6))
plt.plot(x, y, linewidth=2, color='blue')
# Custom x-axis ticks
x_ticks = np.array([0, np.pi/2, np.pi, 3*np.pi/2, 2*np.pi])
x_labels = ['0', 'π/2', 'π', '3π/2', '2π']
plt.xticks(x_ticks, x_labels, fontsize=12)
# Custom y-axis ticks
y_ticks = np.array([-1, -0.5, 0, 0.5, 1])
plt.yticks(y_ticks, fontsize=12)
plt.xlabel('Angle', fontsize=12)
plt.ylabel('sin(x)', fontsize=12)
plt.title('Sine Wave with Custom Ticks', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3)
plt.show()