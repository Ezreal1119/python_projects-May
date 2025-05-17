'''
Author: Patrick Xu
Time: 2025-05-17
Description: This is a useful text editor.
'''


class TextEditor:
    def __init__(self):
        ...

    def get_filename(self):
        while True:
            filename = input(
                '\nEnter the filename to open or create: ').strip()
            if filename == '/':
                print('Invalid filename!')
                continue
            return filename

    def operate_file(self, text, filename, mode):
        with open(filename, mode=mode, encoding='utf-8') as file:
            file.write(text)
        if mode == 'w':
            print(f'{filename} written successfully!')
        elif mode == 'a':
            print(f'{filename} added successfully!')

    def get_text(self, filename):
        line_list = []
        print('Please enter text: ')
        while True:
            line = input().strip()
            if line in ('SAVE', 'ADD'):
                text = '\n'.join(line_list) + '\n'
                mode = 'w' if line == 'SAVE' else 'a'
                self.operate_file(text, filename=filename, mode=mode)
                break
            else:
                line_list.append(line)

    def main(self):
        filename = self.get_filename()
        self.get_text(filename)


if __name__ == '__main__':
    editor = TextEditor()
    editor.main()
