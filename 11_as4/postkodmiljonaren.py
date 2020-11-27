import os

INSTRUCTIONS = '''Welcome to 'Who wants to be a millionaire'!

This came consists of 15 questions, that gets progressively harder, but also
comes with greater rewards.

As long as you answer correctly you earn more money, but if you answer wrong, 
you lose what you have earned.

After questions 5 and 10 you get a guarantee that you will get at least that amount, even if
you fail a later question.

You are free to give up at any time (by answering with 'q') and you walk away with what you have earned.

Press return to begin...
'''

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
        return int(answer) - 1 == self.correct_answer

    def get_correct(self):
        return self.choices[self.correct_answer]

def load_questions(directory = os.path.dirname(__file__)):
    question_file = open(directory + os.sep + 'questions.txt', 'r')
    choice_file = open(directory + os.sep + 'choices.txt', 'r')
    answer_file = open(directory + os.sep + 'answers.txt', 'r')
    prize_file = open(directory + os.sep + 'prize.txt', 'r')

    questions = []

    for _ in range(15):
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
            answer = input('==> ')
            if answer in ('q', '1', '2', '3', '4'):
                return answer

            print('Ogiltigt svar, försök igen')
        except ValueError:
            print('Ogiltigt svar, försök igen')

def main():
    try:
        questions = load_questions()
    except (IOError, FileNotFoundError) as e:
        print('Failed to load questions:', e)
        exit(1)

    guaranteed = 0

    input(INSTRUCTIONS)

    for q in range(15):
        current_question = questions[q]

        print(f'Question {q + 1} for {current_question.prize}')
        current_question.print()
        answer = get_answer()

        if answer == 'q':
            print(f'Thanks for playing, you get to take {questions[q-1].prize} home.')
            break

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
