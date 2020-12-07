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
    '''Class for storing a question with muliple answers, whith functions for
    printing the question to stdout, validating the answer, and getting the correct answer'''
    def __init__(self, question, choices, correct_answer, prize):
        self.question = question
        self.choices = choices
        self.correct_answer = correct_answer
        self.prize = prize

    def print(self):
        '''Prints the question and alternatives'''
        print(self.question)
        for i in range(len(self.choices)):
            print(f'{i + 1}. {self.choices[i]}')

    def validate_answer(self, answer):
        '''Validate if the input answer is correct'''
        return int(answer) == self.correct_answer

    def get_correct(self):
        '''Return the correct answer'''
        return self.choices[self.correct_answer - 1]

def load_questions(path = os.path.dirname(__file__)):
    '''Read from different files and construct the questions'''
    # Add dir separator to path if necessary
    if not path.endswith(os.sep):
        path = path + os.sep

    questions = []

    # Open files for reading
    with open(path + 'questions.txt', 'r') as question_file, \
        open(path + 'choices.txt', 'r') as choice_file, \
        open(path + 'answers.txt', 'r') as answer_file, \
        open(path + 'prize.txt', 'r') as prize_file:

        # Iterate through the files and construct questions
        for _ in range(15):
            question = question_file.readline().strip()
            choices = []
            for _ in range(4):
                choices.append(choice_file.readline().strip())
            answer = int(answer_file.readline().strip())
            prize = int(prize_file.readline().strip())

            questions.append(Question(question, choices, answer, prize))

    return questions

def get_answer():
    '''Reads and validates user input'''
    while True:
        answer = input('==> ')
        if answer in ('q', '1', '2', '3', '4'):
            return answer

        print('Ogiltigt svar, försök igen')

def main():
    # Try to load questions, exit on failiure
    try:
        questions = load_questions()
    except (IOError, FileNotFoundError) as e:
        print('Failed to load questions:', e)
        exit(1)

    # At the beginning, the player isn't guaranteed any prize
    guaranteed = 0

    # Print instructions and wait for the player to start the game
    input(INSTRUCTIONS)

    for index, question in enumerate(questions):
        # Print the question and wait for answer
        print(f'Question {index + 1} for {question.prize}')
        question.print()
        answer = get_answer()

        # Exit the game if the player demands, and shaw the prize for the previous question
        if answer == 'q':
            print(f'Thanks for playing, you get to take {0 if index == 0 else questions[index-1].prize} home.')
            break

        # Check if the answer is correct
        if question.validate_answer(answer):
            # If it's the last question
            if index == 14:
                print('YOU WON!!!!! YOU\'RE A MILLIONAIRE!!!!!!!!!!')
            else:
                print('Right answer!\n')
                # Update the guaranteed prize if at question 5 or 10 (index 4 resp 9)
                if index % 5 == 4:
                    guaranteed = question.prize
        else:
            # Wrong answer, print out the prize, the correct answer and then exit
            print('Sorry, that is the wrong answer, ', end='')

            if guaranteed == 0:
                print('you will go home empty handed.')
            else:
                print(f'you get to take {guaranteed} home.')

            print(f'The right answer was {question.get_correct()}')
            break

main()
