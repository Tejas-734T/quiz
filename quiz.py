# Quiz Application

def run_quiz():
    questions = [
        {
            "question": "What is the capital of India?",
            "options": ["A. Mumbai", "B. Delhi", "C. Chennai", "D. Kolkata"],
            "answer": "B"
        },
        {
            "question": "Which language is used for AI?",
            "options": ["A. Python", "B. HTML", "C. CSS", "D. SQL"],
            "answer": "A"
        },
        {
            "question": "Who invented Python?",
            "options": ["A. James Gosling", "B. Dennis Ritchie", "C. Guido van Rossum", "D. Elon Musk"],
            "answer": "C"
        },
        {
            "question": "Which is not a data type in Python?",
            "options": ["A. List", "B. Tuple", "C. Integer", "D. Character"],
            "answer": "D"
        },
        {
            "question": "Which symbol is used for comments in Python?",
            "options": ["A. //", "B. /* */", "C. #", "D. --"],
            "answer": "C"
        }
    ]

    score = 0

    print("\n📘 Welcome to the Quiz Application!\n")

    for i, q in enumerate(questions, start=1):
        print(f"Q{i}. {q['question']}")
        
        for option in q["options"]:
            print(option)

        user_answer = input("Enter your answer (A/B/C/D): ").upper()

        if user_answer == q["answer"]:
            print(" Correct!\n")
            score += 1
        else:
            print(f" Wrong! Correct answer is {q['answer']}\n")

    print(" Quiz Completed!")
    print(f"Your Score: {score}/{len(questions)}")

    percentage = (score / len(questions)) * 100
    print(f"Percentage: {percentage:.2f}%")

    if percentage >= 80:
        print(" Excellent!")
    elif percentage >= 50:
        print(" Good Job!")
    else:
        print(" Keep Practicing!")


# Run the quiz
run_quiz()