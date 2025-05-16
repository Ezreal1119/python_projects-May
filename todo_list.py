'''
Author: Patrick Xu
Time: 2025-05-17
Description: This is a useful todo list application.
'''

import pandas as pd
import os
from termcolor import cprint
import re
from datetime import datetime


class TodoList:

    FOLDER_PATH = os.path.join('record/', 'todo_list/')
    PATH = os.path.join(FOLDER_PATH, 'record.csv')

    def __init__(self):
        ...
        # task, work/personal, created_at, completed

        try:
            self.df = pd.read_csv(self.PATH)
        except FileNotFoundError:
            if not os.path.exists(self.FOLDER_PATH):
                os.makedirs(os.path.join('record/', 'todo_list/'))
            self.df = pd.DataFrame(
                columns=['task', 'type', 'created_at', 'completed'])
            self.df.to_csv(self.PATH, index=False)

    def menu_display(self):
        print('\nTodo List Menu:')
        print('1. View tasks')
        print('2. Add a task')
        print('3. Complete a task')
        print('4. Remove a task')
        print('5. Exit')

    def get_choice(self, message, choices):
        while True:
            choice = input(message).strip().lower()
            if choice not in choices:
                print('Invalid choice!')
                continue
            return choice

    def get_work_or_personal(self):
        while True:
            print('\nPlease enter the type: ')
            print('1. work')
            print('2. personal')
            choice = input(': ')
            if choice in ('1', '2'):
                break
            print('Invalid choice!')
        return 'work' if choice == '1' else 'personal'

    def view_task(self, filtered_df=None, display_menu=True):
        if filtered_df is None:
            type = self.get_work_or_personal()
            filtered_df = self.df[self.df.loc[:, 'type'] == type]
            filtered_df = filtered_df.reset_index(drop=True)
        filtered_df = filtered_df.reset_index(drop=True)
        if filtered_df.shape[0] == 0:
            self.menu_display()
            print('\nNo task yet!')
            return False
        if display_menu:
            self.menu_display()
            print('\nTasks:')
        for index in range(filtered_df.shape[0]):
            text = f'{index + 1}. ({
                filtered_df.loc[index, 'type']
            }){
                filtered_df.loc[index, 'task']
            } - {
                filtered_df.loc[index, 'created_at']
            }'
            if filtered_df.loc[index, 'completed'] == 'y':
                cprint(text, color='white', on_color='on_green')
            else:
                print(text)
        return True

    def add_task(self):
        while True:
            task = input('\nPlease enter the task: ')
            if re.search(r'[a-zA-Z]', task) is not None:
                break
            print('Invalid task!')
        while True:
            print('\nPlease enter the type: ')
            print('1. work')
            print('2. personal')
            choice = input(': ')
            if choice in ('1', '2'):
                break
            print('Invalid choice!')
        type = 'work' if choice == '1' else 'personal'
        created_at = datetime.now().strftime('%m-%d %H:%M')
        completed = 'n'
        df = pd.DataFrame(
            [(task, type, created_at, completed)],
            columns=self.df.columns
        )
        self.df = pd.concat([self.df, df], ignore_index=True)
        self.df.to_csv(self.PATH, index=False)
        self.menu_display()
        print('\nTask added successfully!')

    def complete_task(self):
        type = self.get_work_or_personal()
        filtered_df = self.df[self.df.loc[:, 'type'] == type]
        print('\nWhich task you have completed?')
        if not self.view_task(filtered_df=filtered_df, display_menu=False):
            return
        choice = self.get_choice(
            ': ',
            choices=[str(i + 1) for i in range(filtered_df.shape[0])]
        )
        self.menu_display()
        if filtered_df.iloc[int(choice) - 1]['completed'] == 'y':
            print('\nTask already completed!')
        else:
            self.df.loc[filtered_df.index[int(choice) - 1], 'completed'] = 'y'
            self.df.to_csv(self.PATH, index=False)
            print('\nTask completed!')

    def remove_task(self):
        type = self.get_work_or_personal()
        filtered_df = self.df[self.df.loc[:, 'type'] == type]
        print('\nWhich task you want to delete?')
        if not self.view_task(filtered_df=filtered_df, display_menu=False):
            return
        choice = self.get_choice(
            ': ',
            choices=[str(i + 1) for i in range(filtered_df.shape[0])]
        )
        self.df = self.df.loc[self.df.index !=
                              filtered_df.index[int(choice) - 1]]
        self.df.reset_index(drop=True)
        self.df.to_csv(self.PATH, index=False)
        self.menu_display()
        print('\nTask removed successfully!')

    def main(self):
        self.menu_display()
        choice = self.get_choice(
            '\nEnter your choice: ',
            choices=[str(i) for i in range(1, 6)]
        )
        while True:
            if choice == '1':
                self.view_task()
            elif choice == '2':
                self.add_task()
            elif choice == '3':
                self.complete_task()
            elif choice == '4':
                self.remove_task()
            elif choice == '5':
                print('\nGoodbye\n')
                break
            choice = self.get_choice(
                '\nEnter your choice: ',
                choices=[str(i) for i in range(1, 6)]
            )


if __name__ == '__main__':
    app = TodoList()
    app.main()
