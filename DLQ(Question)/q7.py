# 7. Nested Dictionary Report
# Store student scores in nested dictionaries and print averages.
#we can also take input aswell 
students = {
    "Ritesh": {"Math": 85, "Science": 90, "English": 78},
    "Raju": {"Math": 75, "Science": 80, "English": 88},
    "Ayush": {"Math": 95, "Science": 85, "English": 92}
}
for student, scores in students.items():
    total_score = sum(scores.values())
    average_score = total_score / len(scores)
    print(f"{student}'s Average Score: {average_score:.2f}")