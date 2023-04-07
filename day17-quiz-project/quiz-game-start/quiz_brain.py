class QuizBrain:

    def __init__(self, questions):
        self.question_number = 0
        self.questions = questions
        self.score = 0
        self.max_score = 0

    def still_has_questions(self):
        return self.question_number < len(self.questions)

    def next_question(self):
        question = self.questions[self.question_number]
        self.question_number += 1
        self.max_score += 100
        answer = input(
                f'Q{self.question_number}. {question.text} (True/False)?: '
            )
        if answer == question.answer:
            self.score += 100
            print(f'Correct! Score: {self.score}/{self.max_score}')
        else:
            print(
                    'Sorry, incorrect answer. Score: ' +
                    f'{self.score}/{self.max_score}'
                )

    def end_game(self):
        print('Game ended')
        if self.score > self.max_score/2:
            print(
                    f'Congratulations, Your score was {self.score}' +
                    f' out of {self.max_score}!'
                )
        else:
            print(f'Your score was only {self.score}/{self.max_score}')
