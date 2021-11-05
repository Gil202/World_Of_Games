from random import randrange


def generate_number(diff):
    secret_number = randrange(1, diff+1)
    return secret_number


def get_guess_from_user(diff):
    valid = 0
    while valid == 0:
        try:
            thechoice = int(input(f"Guess a number between 1 and {diff} \n"))
            if 0 < thechoice <= diff:
                valid = 1
                return thechoice
            else:
                print("***out of bounds*** \n")
        except ValueError:
            print("Please guess a *number* \n")


def compare_results(theguess, theanswer):
    print(f"Your guess was {theguess}, the answer is {theanswer}")
    if theguess == theanswer:
        print(theguess)
        print("WIN")
        return True
    else:
        print(theguess)
        print("FAIL")
        return False


def play(diff):
    num = generate_number(diff)
    guess = get_guess_from_user(diff)
    res = compare_results(guess, num)
    return res
