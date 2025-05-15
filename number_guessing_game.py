'''
Author: Patrick Xu
Time: 2025-05-15
Description: This is an interesting number guessing game.
'''

import os
import random
class NumberGuessingGame:

    def __init__(self, max_round=10):
        self.min = 0
        self.max = 100
        self.max_round = max_round
        path = 'record/number_guessing_game/'
        if not os.path.exists(path):
            os.makedirs(path)
        try:
            with open(path + 'history_best_score', mode='r', encoding='utf-8') as file:
                self.best_score = int(file.read())
        except OSError:
            with open(path + 'history_best_score', mode='w', encoding='utf-8') as file:
                file.write('10')
            self.best_score = 10

    def get_min_and_max(self):
        while True:

            try:
                min = int(input('\nPlease enter the lower bound: ').strip())
                max = int(input('Please enter the upper bound: ').strip())
                if min >= max:
                    raise RuntimeError(
                        '\nLower bound can not be greater than or equal to upper bound!'
                    )
                return (min, max)
            except ValueError:
                print('\nPlease enter valid integer!')
            except RuntimeError as e:
                print(e)

    def get_valid_number(self):
        while True:
            number = input(f'\nPlease enter a number between {self.min}-{self.max}: ').strip()
            try:
                number = int(number)
                if number < self.min or number > self.max:
                    raise RuntimeError('Please enter valid number in between!')
                return number
            except ValueError:
                print('Please enter a valid number')
            except RuntimeError as e:
                print(e)

    def game_body(self):
        count = 0
        while True:
            if count == self.max_round:
                print(f'You tried too many times! The answer is {self.answer}.')
                break
            number = self.get_valid_number()
            count += 1
            if number < self.answer:
                print('Higher!')
            elif number > self.answer:
                print('Lower!')
            else:
                print(f'\nYou nailed it with {count} attempts!')
                if count < self.best_score:
                    print('Congratutions! You broke the record!')
                    with open(
                        'record/number_guessing_game/history_best_score',
                        mode='w',
                        encoding='utf-8'
                    ) as file:
                        file.write(str(count))
                print(f'(History best score is {self.best_score})\n')
                break



    def main(self):
        print('Welcome to the number guessing game!')
        self.min, self.max = self.get_min_and_max()
        self.answer = random.randint(self.min, self.max)
        self.game_body()

if __name__ == '__main__':

    game = NumberGuessingGame()
    game.main()