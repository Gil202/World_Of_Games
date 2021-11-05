import MemoryGame
import GuessGame
import CurrencyRouletteGame
import Score


def welcome(name):
    print(f"Hello {name} and welcome to the World of Games (WoG) \n Here you can find many cool games to play")


def load_game():
    diffi = 10
    choice = 10

    # Get game of choice
    while (choice < 1) or (choice > 3):
        try:
            choice = int(input("Please choose a game to play \n"
                               "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back \n"
                               "2. Guess Game - guess a number and see if you chose like the computer \n"
                               "3. Currency Roulette - try and guess the value of random amount of USD in ILS \n"))
            if (choice < 1) or (choice > 3):
                print("*** PLease choose a number between 1-3 *** \n")
        except ValueError:
            print("*** Please use numbers *** \n")

    # Get difficulty
    while (diffi < 1) or (diffi > 6):
        try:
            diffi = int(input("Please choose game difficulty from 1 to 5 \n"))
            if (diffi < 1) or (diffi > 6):
                print("***Please enter a number between 1-5*** \n")
        except ValueError:
            print("*** Please use numbers *** \n")

    # Run game
    if choice == 1:
        gameresult = MemoryGame.play(diffi)
    elif choice == 2:
        gameresult = GuessGame.play(diffi)
    elif choice == 3:
        gameresult = CurrencyRouletteGame.play(diffi)

    # Add score
    if gameresult == True:
        Score.add_score(diffi)
