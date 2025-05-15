'''
Author: Patrick Xu
Time: 2025-05-15
Description: This is an interesting and meaningful quiz game
'''

import os
import pandas as pd
from termcolor import cprint


class QuizGame:

    QUESTION_DIR = 'quiz_questions/'
    SUBJECT_PATH_MAPPING = {
        '1': 'geography_questions.csv',
        '2': 'history_questions.csv',
        '3': 'science_questions.csv'
    }

    def __init__(self):
        ...

    def get_subject(self):
        while True:
            print('\nPlease select one subject: ')
            print('1. Geography')
            print('2. History')
            print('3. Science')
            choice = input(': ').strip()
            if choice not in [str(i) for i in range(1, 4)]:
                print('Invalid choice!')
                continue
            return choice

    def get_difficulty(self):
        while True:
            choice = input('\nPlease enter difficulty level: (1-3) ').strip()
            if choice not in [str(i) for i in range(1, 4)]:
                print('Invalid choice!')
                continue
            return choice

    def load_questions(self, subject, difficulty):
        subject_path = self.SUBJECT_PATH_MAPPING.get(subject)
        df = pd.read_csv(os.path.join(self.QUESTION_DIR, subject_path))
        df = df[df.loc[:, df.columns[5]] == int(difficulty)]
        df = df.reset_index(drop=True)
        return df

    def display_question(self, df, index):
        print(f'\n{df.loc[index, df.columns[0]]}')
        print('A. ', df.loc[index, df.columns[1]])
        print('B. ', df.loc[index, df.columns[2]])
        print('C. ', df.loc[index, df.columns[3]])
        print('D. ', df.loc[index, df.columns[4]])

    def get_choice(self):
        while True:
            choice = input('Your choice: ').strip().lower()
            if choice not in ('a', 'b', 'c', 'd'):
                print('\nInvalid choice!\n')
                continue
            return choice

    def game_body(self, df):
        total_count = correct_count = 0
        for i in range(10):
            self.display_question(df, i)
            choice = self.get_choice()
            correct_answer = df.loc[i, df.columns[-1]]
            if choice == correct_answer.lower():
                cprint('Correct!', color='green')
                correct_count += 1
            else:
                cprint(
                    f'Wrong! The correct answer is {correct_answer}.', color='red')
            total_count += 1
            print(
                f'(Total questions: {total_count}, correct: {correct_count})')
        return correct_count

    def main(self):
        subject = self.get_subject()
        difficulty = self.get_difficulty()
        df = self.load_questions(subject, difficulty)
        correct_count = self.game_body(df)
        cprint(
            f'\nYou final score is {correct_count * 10}\n', color='blue', attrs=['bold'])


if __name__ == '__main__':
    game = QuizGame()
    game.main()
