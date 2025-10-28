#1. Student Performance Analyzer
# Store names and scores of 5 students, calculate average and top scorer.
students = {}
for _ in range(5):
    name = input("Enter student name: ")
    score = float(input("Enter student score: "))
    students[name] = score
average_score = sum(students.values()) / len(students)
top_guy = max(students, key=students.get)
print(f"Average Score: {average_score}")
print(f"Top Scorer: {top_guy} with score {students[top_guy]}")
#Output:
# Enter student name: Ritesh
# Enter student score: 85
# Enter student name: Anjali
# Enter student score: 92
# Enter student name: Vikram
# Enter student score: 78
# Enter student name: Priya
# Enter student score: 88
# Enter student name: Neha
# Enter student score: 95
# Average Score: 87.6
# Top Scorer: Neha with score 95.0