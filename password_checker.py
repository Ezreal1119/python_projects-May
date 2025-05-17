'''
Author: Patrick Xu
Time: 2025-05-17
Description: This is a useful passwork checker.
'''

import re


class PasswordChecker:
    def __init__(self):
        ...

    def check_strength(self):
        while True:
            strength = 0
            password = input('Enter a password: ').strip()
            if len(password) == 0:
                print('Invalid password!')
                continue
            if re.search(r'[0-9]', password) is not None:
                strength += 1
            if re.search(r'[a-z]', password) is not None:
                strength += 1
            if re.search(r'[A-Z]', password) is not None:
                strength += 1
            if re.search(r'[^\w]', password) is not None or \
                    re.search(r'_', password) is not None:
                strength += 1
            if len(password) >= 8:
                strength += 1
            return strength

    def get_strength_level(self, strength):
        if strength == 1:
            strength_level = 'Very weak'
        elif strength == 2:
            strength_level = 'Weak'
        elif strength == 3:
            strength_level = 'Medium'
        elif strength == 4:
            strength_level = 'Strong'
        elif strength == 5:
            strength_level = 'Very strong'
        return strength_level

    def main(self):
        strength = self.check_strength()
        strength_level = self.get_strength_level(strength)
        print(f'Password strength: {strength_level}')


if __name__ == '__main__':
    checker = PasswordChecker()
    checker.main()
