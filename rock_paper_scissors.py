'''
Author: Patrick Xu
Time: 2025-05-15
Description: This is an interesting rock paper scissor game.
'''

import random

class RockPaperScissors:

    ROCK = 'r'
    PAPER = 'p'
    SCISSORS = 's'

    def __init__(self):
        ...
    
    def get_choice(self):
        while True:
            choice = input('\nRock, paper, or scissors? (r/p/s) ' ).strip().lower()
            if choice not in (self.ROCK, self.PAPER, self.SCISSORS):
                print('Invalid choice!')
                continue
            return choice
        
    def one_round(self):
        user_choice = self.get_choice()
        computer_choice = random.choice([self.ROCK, self.PAPER, self.SCISSORS])
        print(f'You chose {user_choice}')
        print(f'Computer chose {computer_choice}')
        return self.get_result(user_choice, computer_choice)
    
    def get_result(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            print('It\'s a draw.')
            return 'draw'
        if (user_choice, computer_choice) in (
                (self.ROCK, self.SCISSORS),
                (self.PAPER, self.ROCK),
                (self.SCISSORS, self.PAPER)
            ):
            print('You won!')
            return 'user'
        print('Computer won!')
        return 'computer'


    def best_of_three(self):
        user_win = computer_win = 0
        while True:
            result = self.one_round()
            if result == 'user':
                user_win += 1
            elif result == 'computer':
                computer_win += 1
            if user_win == 2:
                return 'user'
            if computer_win == 2:
                return 'computer'
            
    def game_body(self):
        result = self.best_of_three()
        if result == 'user':
            print('\nCongrats! You won the bo3.')
        elif result == 'computer':
            print('\nWhat a pity. Computer won the bo3.')
        return result

    def play_again(self):
        while True:
            choice = input('\nWould you like to play again? (y/n) ')
            if choice == 'y':
                return True
            elif choice == 'n':
                return False
            else:
                print('Invalid choice!')

    def main(self):
        total_user_win = total_computer_win = 0
        while True:
            if self.game_body() == 'user':
                total_user_win += 1
            else:
                total_computer_win += 1
            print(f'(Standings: user: {total_user_win}, computer: {total_computer_win})')
            if not self.play_again():
                break




            






if __name__ == '__main__':
    game = RockPaperScissors()
    game.main()