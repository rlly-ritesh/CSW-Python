import numpy as np

# Define input array
x = np.array([1, 2, 3, 4, 5])

# Compute advanced mathematical functions
exp_values = np.exp(x)         # Exponential (e^x)
log_values = np.log(x)         # Natural logarithm (ln)
log10_values = np.log10(x)     # Base-10 logarithm
sqrt_values = np.sqrt(x)       # Square root

# Display results
print("Original array:       ", x)
print("Exponential (e^x):    ", np.round(exp_values, 4))
print("Natural log (ln(x)):  ", np.round(log_values, 4))
print("Base-10 log:          ", np.round(log10_values, 4))
print("Square root:          ", np.round(sqrt_values, 4))