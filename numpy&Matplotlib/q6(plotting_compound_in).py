import numpy as np
import matplotlib.pyplot as plt

# Parameters
principal = 1000  # Initial investment
rates = [0.03, 0.05, 0.07, 0.10]  # Different interest rates
years = np.arange(0, 31)  # Time span: 0 to 30 years

# Plot compound interest growth for different rates
plt.figure(figsize=(10, 6))
for rate in rates:
    amount = principal * (1 + rate) ** years
    plt.plot(years, amount, label=f'{rate*100:.0f}% interest', linewidth=2)

# Customize plot
plt.xlabel('Years', fontsize=12)
plt.ylabel('Amount ($)', fontsize=12)
plt.title('Compound Interest Growth Over Time', fontsize=14, fontweight='bold')
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()

# Calculate and display specific example for 5% interest over 10 years
rate = 0.05
years_calc = np.arange(0, 11)
amount = principal * (1 + rate) ** years_calc

print("Year\tAmount")
print("-" * 20)
for year, amt in zip(years_calc, amount):
    print(f"{year}\t${amt:.2f}")