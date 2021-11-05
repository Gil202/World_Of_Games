import os


def add_score(diffi):
    if not os.path.isfile('./Scores.txt'):
        thefile = open("Scores.txt","w+")
        thefile.write("0")
        thefile.close()

    thefile = open("Scores.txt","r+")
    currentscore = int(thefile.read())
    currentscore = currentscore + (diffi*3+5)
    thefile.seek(0)
    thefile.write(str(currentscore))
    thefile.close()