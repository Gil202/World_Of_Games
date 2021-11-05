from currency_converter import CurrencyConverter
from random import randrange

rates = CurrencyConverter()


def get_money_interval(diff):
    thedollar = randrange(1, 100)
    print(f'{thedollar} dollars')
    thenis = rates.convert(thedollar, 'USD', 'ILS')
    botval = thenis - (5 - diff)
    topval = thenis + (5 - diff)
    return round(botval, 2), round(topval,2)


def get_guess_from_user():
    valid = 0
    while valid == 0:
        try:
            theguess = float(input("Guess how many ILS this sum of dollars is worth \n"))
            return theguess
        except ValueError:
            print("***Illegal input!*** \n")


def play(diff):
    vals = get_money_interval(diff)
    guess = get_guess_from_user()
    if vals[0] <= guess <= vals[1]:
        print(vals)
        print("WIN")
        return True
    else:
        print(vals)
        print("FAIL")
        return False