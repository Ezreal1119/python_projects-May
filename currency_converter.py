'''
Author: Patrick Xu
Time: 2025-05-15
Description: This is a useful currenty converter.
'''


class CurrencyConverter:

    USD = 'usd'
    CNY = 'cny'
    CAD = 'cad'
    EUR = 'eur'
    CURRENCY_LIST = [USD, CNY, CAD, EUR]
    CONVERSION = {
        ('usd', 'usd'): 1,
        ('usd', 'cny'): 7.21,
        ('usd', 'cad'): 1.4,
        ('usd', 'eur'): 0.89
    }

    def __init__(self):
        ...

    def get_amount(self):
        while True:
            try:
                amount = input('Please enter the amount: ').strip()
                amount = float(amount)
                return amount
            except ValueError:
                print('Invalid amount!')

    def get_currency(self):
        while True:
            currency = input(
                'Please enter the curreny? (USD/CNY/CAD/EUR) ').strip().lower()
            if currency not in self.CURRENCY_LIST:
                print('Invalid currency!')
                continue
            return currency

    def converter_body(self):
        amount = self.get_amount()
        currency = self.get_currency()
        currency_list = [c for c in self.CURRENCY_LIST if c != currency]
        for cur in currency_list:
            exchange_rate = self.CONVERSION.get(('usd', cur)) / \
                self.CONVERSION.get(('usd', currency))
            print(f'{currency.upper()} to {cur.upper()} is: 1 : {exchange_rate:.2f}')

    def main(self):
        self.converter_body()


if __name__ == '__main__':
    converter = CurrencyConverter()
    converter.main()
