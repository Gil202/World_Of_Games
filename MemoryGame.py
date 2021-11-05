from random import randrange
from time import sleep

def generate_sequence(diff):
    thelist = []
    while len(thelist) != diff:
        thelist.append(randrange(1, 101))
    print(thelist)
    sleep(1)
    print('\n' * 80)
    return thelist


def get_list_from_user(diff):
    thememlist = []
    print("type in your numbers (one by one) \n")
    while len(thememlist) != diff:
        try:
            thememlist.append(int(input()))
        except ValueError:
            print("***Make sure you hit Enter after inserting each number*** \n")
    return thememlist


def is_list_equal(gen_seq, player_seq):
    if gen_seq == player_seq:
        return True
    else:
        return False


def play(diff):
    board = generate_sequence(diff)
    guess = get_list_from_user(diff)
    result = is_list_equal(board, guess)
    if result:
        print(board)
        print("WIN")
        return True
    else:
        print(board)
        print("FAIL")
        return False