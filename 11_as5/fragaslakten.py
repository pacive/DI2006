import os
import re

# Regexes for matching questions and answers in a file
QUESTION_REGEX = re.compile(r'^\d+\. (.*)\(\d answers\)\n')
ANSWER_REGEX = re.compile(r'^(.*) \((\d+) points\)\n')

class Question():
    '''Class representing a question in the family feud game'''

    def __init__(self, question):
        '''Create a new Question instance'''
        self.question = question
        self.answers = []
        self.scores = []
        self.correct = []

    def add_answer(self, answer, score):
        '''Add an answer, with a corresponding score'''
        self.answers.append(answer)
        self.scores.append(score)
        self.correct.append(False)

    def print_answers(self):
        '''Print out the answers that the player got right, or just a number for the rest'''
        for i in range(len(self.answers)):
            if self.correct[i]:
                print(f'{self.answers[i]} - {self.scores[i]} points')
            else:
                print(i + 1)

    def match_answer(self, answer):
        '''Check if the provided answer is correct, and updates state accordingly'''
        for i in range(len(self.answers)):
            if answer.lower() == self.answers[i].lower():
                self.correct[i] = True
                return True
        return False

    def num_answers(self):
        '''Gets the number of answers'''
        return len(self.answers)

    def get_score(self):
        '''Get the total score of the correct answers'''
        score = 0
        for i in range(len(self.answers)):
            if self.correct[i]:
                score += self.scores[i]
        return score

def load_questions(path = os.path.dirname(__file__)):
    '''Loads questions from a file'''
    # Add dir separator to path if necessary
    if not path.endswith(os.sep):
        path = path + os.sep

    questions = []

    with open(path + 'questions.txt', 'r') as question_file:
        while line := question_file.readline():
            # Create a new question if the line matches
            if match := QUESTION_REGEX.match(line):
                questions.append(Question(match.group(1)))
            # Otherwise, add it as an answer to the last created question
            elif match := ANSWER_REGEX.match(line):
                questions[-1].add_answer(match.group(1), int(match.group(2)))

    return questions

def play_round(question):
    '''Play a round of the game'''
    print(question.question)
    for _ in range(question.num_answers()):
        question.print_answers()
        answer = input('==> ')
        if not question.match_answer(answer):
            print('\nSorry, wrong answer\n')

    return question.get_score()

def main():
    scores = [0, 0]
    questions = load_questions()
    rounds = 0

    while True:
        # Ask how many rounds should be played and check if it's valid
        try:
            rounds = int(input('How many rounds should each player play? '))
            if rounds in range(len(questions) // 2 + 1):
                break
        finally:
            print(f'Please input a value between 1 and {len(questions) // 2}')

    print()

    for i in range(rounds * 2):
        # Alternate between 0 and 1
        player = i % 2

        print(f'\nRound - {i + 1}\n')
        print('##############')
        print(f'Player 1: {scores[0]} points')
        print(f'Player 2: {scores[1]} points')
        print('##############\n')
        print(f'Player {player + 1} Plays')

        # Play a round and add to the player's score
        scores[player] += play_round(questions[i])

    # Find out who won
    if scores[0] > scores[1]:
        print('Player 1 wins')
    elif scores[0] < scores[1]:
        print('Player 2 wins')
    else:
        print('It\'s a tie')
    print(f'{max(scores)} to {min(scores)}')

main()
