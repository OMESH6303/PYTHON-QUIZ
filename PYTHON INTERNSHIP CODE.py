# Quiz Game

questions = {
    "What is the capital of France?": ["London", "Paris", "Berlin", "Madrid"],
    "Who wrote 'Hamlet'?": ["Shakespeare", "Milton", "Dickens", "Wilde"],
    "What is the largest mammal?": ["Elephant", "Whale", "Giraffe", "Lion"]
}

def ask_question(question, options, correct_answer):
    print(question)
    for idx, option in enumerate(options):
        print(f"{idx + 1}. {option}")
    user_answer = input("Enter your answer (1-4): ")
    if user_answer.isdigit() and 1 <= int(user_answer) <= 4:
        user_answer_index = int(user_answer) - 1
        if options[user_answer_index] == correct_answer:
            print("Correct!")
            return 1
        else:
            print(f"Wrong! The correct answer is: {correct_answer}")
            return 0
    else:
        print("Invalid input. Please enter a number from 1 to 4.")
        return 0

def run_quiz(questions):
    total_score = 0
    for question, options in questions.items():
        correct_answer = options[1]  # Assuming the correct answer is always the second option
        total_score += ask_question(question, options, correct_answer)
    print(f"Quiz completed! Your total score is: {total_score}")

# Running the quiz
run_quiz(questions)
