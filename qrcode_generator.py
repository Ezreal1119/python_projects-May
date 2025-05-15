'''
Author: Patrick Xu
Time: 2025-05-15
Description: This is a useful qrcode generator.
'''

import qrcode
import os


class QrcodeGenerator:
    def __init__(self):
        ...

    def main(self):
        url = input('Enter the text or URL: ').strip()
        filename = input('Enter the file name: ').strip()
        if '.' in filename:
            filename = filename[:filename.find('.')] + '.jpg'
        else:
            filename = filename + '.jpg'
        image = qrcode.make(url)
        image.save(os.path.join('record/qrcode_generator', filename))


if __name__ == '__main__':
    generator = QrcodeGenerator()
    generator.main()
