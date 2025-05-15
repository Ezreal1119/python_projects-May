'''
Author: Patrick Xu
Time: 2025-05-15
Description: This is an interesting tic-tac-toe game.
'''

import time
import random
import copy


class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.first_turn: str

    def board_display(self):
        print()
        horizontal_boarder = '+-+-+-+'
        for i in range(3):
            print(horizontal_boarder)
            print('|' + '|'.join(self.board[i]) + '|')
        print(horizontal_boarder, '\n')

    def get_choice(self, message, choices):
        while True:
            choice = input(message).strip().lower()
            if choice not in choices:
                print('\nInvalid choice!\n')
                continue
            return choice

    def player_move(self):
        print('Your move: ')
        while True:
            player_row = self.get_choice(
                'Please enter row: (1-3) ',
                choices=['1', '2', '3']
            )
            player_column = self.get_choice(
                'Please enter row: (1-3) ',
                choices=['1', '2', '3']
            )
            if self.board[int(player_row) - 1][int(player_column) - 1] != ' ':
                print('This spot has been taken!')
                continue
            self.board[int(player_row) - 1][int(player_column) - 1] = 'X' if self.first_turn == 'player' \
                else 'O'
            break

    def computer_move(self):
        time.sleep(random.uniform(1, 2))
        print('Computer move: ')
        all_spots = [self.board[i][j] for i in range(3) for j in range(3)]
        all_valid_spots = [i for i in range(9) if all_spots[i] == ' ']

        mark = None
        for spot in all_valid_spots:
            copied_board = copy.deepcopy(self.board)
            computer_row = spot // 3
            computer_column = spot % 3
            copied_board[computer_row][computer_column] = 'X' if self.first_turn == 'computer' \
                else 'O'
            result = self.check_result(copied_board)
            if result == 'computer':
                self.board[computer_row][computer_column] = 'X' if self.first_turn == 'computer' \
                    else 'O'
                return
        for spot in all_valid_spots:
            copied_board = copy.deepcopy(self.board)
            player_row = spot // 3
            player_column = spot % 3
            copied_board[player_row][player_column] = 'X' if self.first_turn == 'player' \
                else 'O'
            result = self.check_result(copied_board)
            if result == 'player':
                self.board[player_row][player_column] = 'X' if self.first_turn == 'computer' \
                    else 'O'
                return
        choice = random.choice(all_valid_spots)
        computer_row = choice // 3
        computer_column = choice % 3
        self.board[computer_row][computer_column] = 'X' if self.first_turn == 'computer' \
            else 'O'

    def get_first_turn(self):
        print('Who goes first?')
        print('1. player')
        print('2. computer')
        choice = self.get_choice(': ', choices=['1', '2'])
        if choice == '1':
            self.first_turn = 'player'
        else:
            self. first_turn = 'computer'

    def check_result_helper(self, pattern):
        if pattern == 'X':
            return 'player' if self.first_turn == 'player' else 'computer'
        else:
            return 'player' if self.first_turn == 'computer' else 'computer'

    def check_result(self, board):
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] != ' ':
                return self.check_result_helper(board[i][0])
            if board[0][i] == board[1][i] == board[2][i] != ' ':
                return self.check_result_helper(board[0][i])
        if board[0][0] == board[1][1] == board[2][2] != ' ':
            return self.check_result_helper(board[0][0])
        if board[0][-1] == board[1][-2] == board[2][-3] != ' ':
            return self.check_result_helper(board[0][-1])
        all_spots = [board[i][j] for i in range(3) for j in range(3)]
        if ' ' not in all_spots:
            return 'draw'

    def display_result(self):
        result = self.check_result(self.board)
        if result == 'player':
            print('Congrats! You won the game.\n')
        elif result == 'computer':
            print('What a pity. Computer won!\n')
        elif result == 'draw':
            print('It\'s a draw')
        return result

    def main(self):
        self.get_first_turn()
        self.board_display()
        if self.first_turn == 'computer':
            self.computer_move()
            self.board_display()
        while True:
            self.player_move()
            self.board_display()
            if self.display_result() is not None:
                break
            self.computer_move()
            self.board_display()
            if self.display_result() is not None:
                break


if __name__ == '__main__':
    game = TicTacToe()
    game.main()
