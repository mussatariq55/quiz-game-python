from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
from art import logo

question_bank = []
for qna in question_data:
    question_bank.append(Question(qna["text"], qna["answer"]))

quiz = QuizBrain(question_bank)
print(logo)
while quiz.still_has_question():
    quiz.next_question()
print("Congrats! You have completed the quiz")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")
