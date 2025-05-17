'''
Author: Patrick Xu
Time: 2025-05-17
Description: This is a useful password generator.
'''

import string
import random


class PasswordGenerator:
    def __init__(self):
        ...

    def get_length(self):
        while True:
            length = input('\nEnter password length: (between 3-20) ').strip()
            if length not in [str(i) for i in range(3, 21)]:
                print('Invalid number')
                continue
            return int(length)

    def includes_uppercase(self):
        while True:
            choice = input('Include uppercase letters? (y/n): ')
            if choice == 'y':
                return True
            elif choice == 'n':
                return False
            print('Invalid choice!')

    def includes_number(self):
        while True:
            choice = input('Include numbers? (y/n): ')
            if choice == 'y':
                return True
            elif choice == 'n':
                return False
            print('Invalid choice!')

    def includes_special_character(self):
        while True:
            choice = input('Include special characters? (y/n): ')
            if choice == 'y':
                return True
            elif choice == 'n':
                return False
            print('Invalid choice!')

    def generate_password(self, length, uppercase, number, special_character):
        password_list = []
        choices = string.ascii_lowercase
        if uppercase:
            password_list.append(random.choice(string.ascii_uppercase))
            choices += string.ascii_uppercase
        if number:
            password_list.append(random.choice(string.digits))
            choices += string.digits
        if special_character:
            password_list.append(random.choice(string.punctuation))
            choices += string.punctuation
        return ''.join(password_list) + \
            ''.join(random.choices(choices, k=length-len(password_list)))

    def body(self):
        length = self.get_length()
        includes_uppercase = self.includes_uppercase()
        includes_number = self.includes_number()
        includes_special_character = self.includes_special_character()
        print(f'\nGenerated password: {
            self.generate_password(
                length,
                includes_uppercase,
                includes_number,
                includes_special_character
            )
        }\n')

    def main(self):
        self.body()


if __name__ == '__main__':
    generator = PasswordGenerator()
    generator.main()
