import numpy as np
# Portfolio returns (monthly)
returns = np.array([0.02, -0.01, 0.03, 0.015, -0.005,
0.025, 0.01, -0.02, 0.04, 0.018])

# Calculate metrics
mean_return = np.mean(returns)
std_return = np.std(returns)
cumulative_return = np.prod(1 + returns) - 1
print("Investment Portfolio Analysis")
print("-" * 40)
print(f"Average Monthly Return: {mean_return*100:.2f}%")
print(f"Return Volatility (Std Dev): {std_return*100:.2f}%")
print(f"Cumulative Return: {cumulative_return*100:.2f}%")
print(f"Annualized Return: {mean_return*12*100:.2f}%")
# Sharpe Ratio (assuming risk-free rate of 2% annually)
risk_free_rate = 0.02 / 12 # Monthly
sharpe_ratio = (mean_return - risk_free_rate) / std_return
print(f"Sharpe Ratio: {sharpe_ratio:.3f}")