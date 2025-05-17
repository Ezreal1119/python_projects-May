'''
Author: Patrick Xu
Time: 2025-05-17
Description: This is an interesting pig-dice game.
'''

import random
import time


class PigDiceGame:
    def __init__(self):
        self.player_score = 0
        self.computer_score = 0
        self.target_score = 0

    def get_choice(self):
        while True:
            choice = input('Roll again? (y/n) ').strip().lower()
            if choice not in ('y', 'n'):
                print('Invalid choice!')
                continue
            return choice

    def get_target_score(self):
        while True:
            target_score = input('Enter the target score: ').strip()
            try:
                target_score = int(target_score)
                if target_score > 1000:
                    raise ValueError('The score is too high')
                if target_score < 10:
                    raise ValueError('The score is too low!')
                return target_score
            except ValueError as e:
                print(e)

    def get_first_turn(self):
        while True:
            print('Who\'s first turn?')
            print('1. Player')
            print('2. Computer')
            choice = input('You choice: ')
            if choice not in ('1', '2'):
                print('Invalid choice!')
                continue
            return 'player' if choice == '1' else 'computer'

    def display_score(self):
        print(
            f'\nCurrent scores: Player: {self.player_score}, Computer: {self.computer_score}'
        )

    def check_result(self):
        self.display_score()
        if self.player_score >= self.target_score:
            print('\nYou won the game!\n')
            return True
        elif self.computer_score >= self.target_score:
            print('\nComputer won the game!\n')
            return True

    def player_turn(self):
        input('\nPlayer\'s turn: (press \'enter\' to start) ')
        sum = 0
        while True:
            dice = random.randint(1, 6)
            print(f'You rolled a {dice}')
            sum += dice
            if dice == 1:
                print('\nOops, you didn\'t earn any score this game.')
                break
            choice = self.get_choice()
            if choice == 'n':
                self.player_score += sum
                print(f'\nYou scored {sum} this turn.')
                break

    def computer_turn(self):
        threshold = (18 - (self.computer_score -
                     self.player_score) * 0.25)
        print('\nComputer\'s turn: ')
        sum = 0
        while True:
            time.sleep(random.uniform(0.5, 1.5))
            if self.computer_score + sum >= self.target_score or (sum >= threshold and
                                                                  self.target_score - self.computer_score > 5):
                print('Computer decided to stop.')
                self.computer_score += sum
                print(f'\nComputer scored {sum} this turn.')
                break
            else:
                dice = random.randint(1, 6)
                print(f'Computer rolled a {dice}')
                sum += dice
                if dice == 1:
                    print(f'\nComputer scored 0 this turn.')
                    break

    def main(self):
        self.target_score = self.get_target_score()
        if self.get_first_turn() == 'computer':
            self.computer_turn()
            if self.check_result():
                return
        while True:
            self.player_turn()
            if self.check_result():
                return
            self.computer_turn()
            if self.check_result():
                return


if __name__ == '__main__':
    game = PigDiceGame()
    game.main()
