import numpy as np
import matplotlib.pyplot as plt

# Generate random data (normal distribution)
np.random.seed(42)
data = np.random.randn(1000) * 10 + 50  # Mean ~50, Std Dev ~10

# Create histogram
plt.figure(figsize=(10, 6))
plt.hist(data, bins=30, color='skyblue', edgecolor='black', alpha=0.7)
plt.xlabel('Value', fontsize=12)
plt.ylabel('Frequency', fontsize=12)
plt.title('Histogram of Random Data', fontsize=14, fontweight='bold')
plt.grid(True, alpha=0.3, axis='y')
plt.show()

# Statistical summary
print("Statistical Summary:")
print(f"Mean:               {np.mean(data):.2f}")
print(f"Median:             {np.median(data):.2f}")
print(f"Standard Deviation: {np.std(data):.2f}")
print(f"Minimum Value:      {np.min(data):.2f}")
print(f"Maximum Value:      {np.max(data):.2f}")