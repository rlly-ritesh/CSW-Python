# 4. Advanced Quiz App
# Store questions and answers in a dictionary, score the user.
questions = {
    "What is the capital of Odisha? ": "Bhubaneswar",
    "What is 2 + 2? ": "4",
    "What is the largest planet in our solar system? ": "Jupiter",
    "ITER is located in which State'? ": "ODISHA",
    "What is the boiling point of water in Celsius? ": "100"
}
score = 0
for question, answer in questions.items():
    user_answer = input(question)
    if user_answer.strip().lower() == answer.strip().lower():
        score += 1
print(f"Your total score is: {score} out of {len(questions)}")
#Purpose 
# This code implements a simple quiz application where questions and their corresponding answers are stored in a dictionary.
# The user is prompted to answer each question, and their score is calculated based on the number of correct answers.
# At the end of the quiz, the user's total score is displayed.

