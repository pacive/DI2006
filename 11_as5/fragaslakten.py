import os
import re

QUESTION_REGEX = re.compile(r'^\d+\.\s(.*)\(\d answers\)$')
ANSWER_REGEX = re.compile(r'^(.*)\s\((\d+) points\)$')

class Question():
    def __init__(self, question):
        self.question = question
        self.answers = []
        self.scores = []
        self.correct = []

    def add_answer(self, answer, score):
        self.answers.append(answer)
        self.scores.append(score)
        self.correct.append(False)

    def print_answers(self):
        for i in range(len(self.answers)):
            if self.correct[i]:
                print(f'{self.answers[i]} - {self.scores[i]} points')
            else:
                print(i + 1)

    def match_answer(self, answer):
        for i in range(len(self.answers)):
            if answer.lower() == self.answers[i].lower():
                self.correct[i] = True
                return True
        return False

    def num_answers(self):
        return len(self.answers)

    def get_score(self):
        score = 0
        for i in range(len(self.answers)):
            if self.correct[i]:
                score += self.scores[i]
        return score

def load_questions(path = os.path.dirname(__file__)):
    # Add dir separator to path if necessary
    if not path.endswith(os.sep):
        path = path + os.sep

    questions = []

    with open(path + 'questions.txt', 'r') as question_file:
        while line := question_file.readline().strip():
            if match := QUESTION_REGEX.match(line):
                questions.append(Question(match.group(1)))
            elif match := ANSWER_REGEX.match(line):
                questions[-1].add_answer(match.group(1), int(match.group(2)))

    return questions

def play_round(question):
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
        rounds = int(input('How many rounds should each player play? '))
        if rounds in range(len(questions) / 2 + 1):
            break
        print(f'Please input a value between 1 and {len(questions) / 2}')

    print()

    for i in range(rounds * 2):
        player = i % 2

        print(f'\nRound - {i + 1}\n')
        print('##############')
        print(f'Player 1: {scores[0]} points')
        print(f'Player 2: {scores[1]} points')
        print('##############\n')
        print(f'Player {player + 1} Plays')

        scores[player] += play_round(questions[i])

    if scores[0] > scores[1]:
        print('Player 1 wins')
    elif scores[0] < scores[1]:
        print('Player 2 wins')
    else:
        print('It\'s a tie')
    print(f'{max(scores)} to {min(scores)}')

main()
