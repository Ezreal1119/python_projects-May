'''
Author: Patrick Xu
Time: 2025-05-17
Description: This is an interesting cows and bulls game.
'''

import random
import os


class CowsAndBullsGame:

    MAX_ROUND = 10
    FOLDER_PATH = os.path.join('record/', 'cows_and_bulls/')
    PATH = os.path.join(FOLDER_PATH, 'history_best_record')

    def __init__(self):
        self.answer = ''.join(random.sample([str(i) for i in range(10)], k=4))
        if not os.path.exists(self.FOLDER_PATH):
            os.makedirs(self.FOLDER_PATH)
        try:
            with open(self.PATH, mode='r') as file:
                self.best_score = int(file.read())
        except FileNotFoundError:
            with open(self.PATH, mode='w') as file:
                file.write(str(10))
                self.best_score = 10

    def get_digit(self):
        while True:
            try:
                guess = input('\nGuess: ').strip()
                int(guess)
                if len(guess) != 4:
                    raise ValueError('Not 4 digits!')
                if len(set(guess)) < 4:
                    raise ValueError('Not 4 digits!')
                return guess
            except ValueError as e:
                print('Invalid guess: ', end='')
                print(e)

    def get_cows(self, guess):
        count = 0
        for digit in guess:
            if digit in self.answer:
                count += 1
        return count

    def get_bulls(self, guess):
        count = 0
        for i in range(4):
            if guess[i] == self.answer[i]:
                count += 1
        return count

    def welcome(self):
        print('I have generated a 4-digit number with unique digits.', end=' ')
        print('Try to guess it!')

    def game_body(self):
        count = 0
        while True:
            guess = self.get_digit()
            count += 1
            if guess == self.answer:
                print(
                    f'\nYou guessed the correct digit with {count} attempts!\n')
                if count < self.best_score:
                    self.best_score = count
                    with open(self.PATH, mode='w', encoding='utf-8') as file:
                        file.write(str(count))
                break
            if count == self.MAX_ROUND:
                print(f'\nToo many attempts! The answer is {self.answer}')
                break
            cows = self.get_cows(guess)
            bulls = self.get_bulls(guess)
            print(f'{cows} cows, {bulls} bulls')

    def main(self):
        self.welcome()
        self.game_body()
        print(f'(History best score is {self.best_score})\n')


if __name__ == '__main__':
    game = CowsAndBullsGame()
    game.main()
