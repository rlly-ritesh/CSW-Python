import numpy as np

# Create a structured array with mixed data types
dtype = [('name', 'U20'), ('age', 'i4'), ('salary', 'f8')]
employees = np.array([
    ('John Doe', 30, 50000.0),
    ('Jane Smith', 25, 55000.0),
    ('Bob Johnson', 35, 60000.0),
    ('Alice Brown', 28, 52000.0),
    ('Charlie Wilson', 32, 58000.0)
], dtype=dtype)

# Display employee records
print("Employee Records:")
print(employees)

# Access individual fields
print("\nNames:", employees['name'])
print("Ages:", employees['age'])
print("Salaries:", employees['salary'])

# Statistical analysis
print("\nStatistical Summary:")
print(f"Average Age: {np.mean(employees['age']):.1f}")
print(f"Average Salary: ${np.mean(employees['salary']):.2f}")
print(f"Min Salary: ${np.min(employees['salary']):.2f}")
print(f"Max Salary: ${np.max(employees['salary']):.2f}")

# Filtering data: High earners with salary > $55,000
high_earners = employees[employees['salary'] > 55000]
print("\nHigh Earners (>$55,000):")
for emp in high_earners:
    print(f" {emp['name']}: ${emp['salary']:.2f}")