import numpy as np
# Compound Interest Calculation
principal = 1000 # Initial investment
rate = 0.05 # 5% annual interest rate
years = np.arange(0, 11) # 0 to 10 years
# Calculate compound interest: A = P(1 + r)^t
amount = principal * (1 + rate) ** years
print("Year\tAmount")
print("-" * 20)

for year, amt in zip(years, amount):
    print(f"{year}\t${amt:.2f}")
print(f"\nTotal growth: ${amount[-1] - principal:.2f}")
print(f"Percentage increase: {((amount[-1] - principal) / principal * 100):.2f}%")