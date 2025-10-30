import numpy as np
import matplotlib.pyplot as plt
# Data
categories = ['Category A', 'Category B', 'Category C',

'Category D', 'Category E']
values = np.array([30, 25, 20, 15, 10])
# Create pie chart
plt.figure(figsize=(10, 8))
colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99', '#ff99cc']
explode = (0.1, 0, 0, 0, 0) # Explode 1st slice
plt.pie(values, labels=categories, colors=colors, autopct='%1.1f%%',
startangle=90, explode=explode, shadow=True)
plt.title('Distribution of Categories', fontsize=14, fontweight='bold')
plt.axis('equal') # Equal aspect ratio ensures circular pie
plt.show()
# Print percentages
print("Category Distribution:")
for cat, val in zip(categories, values):
    percentage = (val / values.sum()) * 100
print(f"{cat}: {percentage:.1f}%")