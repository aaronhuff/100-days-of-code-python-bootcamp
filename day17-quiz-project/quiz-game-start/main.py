import question_model
import data
import quiz_brain

questions = []
for question in data.question_data:
    questions.append(
        question_model.Question(
                question['text'], question['answer']
            )
        )

quiz = quiz_brain.QuizBrain(questions)
while quiz.still_has_questions():
    quiz.next_question()
quiz.end_game()
