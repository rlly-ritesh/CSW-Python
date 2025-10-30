import numpy as np
import matplotlib.pyplot as plt
# Create data
x = np.linspace(0, 10, 100)
y = np.sin(x)
# Create plot
plt.plot(x, y)
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Sine Wave')
plt.grid(True)
plt.show()