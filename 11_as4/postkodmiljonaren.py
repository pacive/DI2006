import os

class Question():
    def __init__(self, question, choices, correct_answer, prize):
        self.question = question
        self.choices = choices
        self.correct_answer = correct_answer - 1
        self.prize = prize

    def print(self):
        print(self.question)
        for i in range(len(self.choices)):
            print(f'{i + 1}. {self.choices[i]}')

    def validate_answer(self, answer):
        return answer - 1 == self.correct_answer

    def get_correct(self):
        return self.choices[self.correct_answer]

def load_questions(directory = os.path.dirname(__file__)):
    question_file = open(directory + os.sep + 'questions.txt', 'r')
    choice_file = open(directory + os.sep + 'choices.txt', 'r')
    answer_file = open(directory + os.sep + 'answers.txt', 'r')
    prize_file = open(directory + os.sep + 'prize.txt', 'r')

    questions = []

    for i in range(15):
        question = question_file.readline().strip()
        choices = []
        for _ in range(4):
            choices.append(choice_file.readline().strip())
        answer = int(answer_file.readline().strip())
        prize = int(prize_file.readline().strip())

        questions.append(Question(question, choices, answer, prize))

    question_file.close()
    choice_file.close()
    answer_file.close()
    prize_file.close()

    return questions

def get_answer():
    while True:
        try:
            answer = int(input('==> '))
            if answer in range(1, 5):
                return answer
            else:
                print('Ogiltigt svar, försök igen')
        except ValueError:
            print('Ogiltigt svar, försök igen')

def main():
    questions = load_questions()
    guaranteed = 0
    for q in range(15):
        current_question = questions[q]
        print(f'Question {q + 1} for {current_question.prize}')
        current_question.print()
        answer = get_answer()
        if current_question.validate_answer(answer):
            if q == 14:
                print('YOU WON!!!!! YOU\'RE A MILLIONAIRE!!!!!!!!!!')
            else:
                print('Right answer!\n')
            if q % 5 == 4:
                guaranteed = current_question.prize
        else:
            print('Sorry, that is the wrong answer, ', end='')
            if guaranteed == 0:
                print('you will go home empty handed.')
            else:
                print(f'you get to take {guaranteed} home.')
            print(f'The right answer was {current_question.get_correct()}')
            break

main()
