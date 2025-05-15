'''
Author: Patrick
Time: 2025-05-15
Decscription: This is an interesting dice rolling game.
'''

import random

class DiceRollingGame:

    

    def __init__(self):
        self.count = 0

    def get_dice_quantity(self) -> str:
        while True:
            dice_count = input('Enter dice quantity: (1-10)').strip()
            if dice_count not in [str(i) for i in range(1, 10)]:
                print('Invalide choice!')
                continue
            return dice_count
    
    def generate_dices(self, count) -> str:
        dice_list = [str(random.randint(1, 6)) for _ in range(int(count))]
        return f'({', '.join(dice_list)})'
        
    def game_starter(self) -> str:
        while True:
            choice = input('Would you like to play the game? (y/n) ').lower().strip()
            if choice not in ('y', 'n'):
                print('Invalid choice!')
                continue
            return choice
    
    def main(self):
        while True:
            if self.game_starter() == 'y':
                dice_count = self.get_dice_quantity()
                print(self.generate_dices(dice_count))
                self.count += 1
                print('count:', self.count)
            else:
                break

if __name__ == '__main__':
    game = DiceRollingGame()
    game.main()