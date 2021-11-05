from flask import Flask

app = Flask(__name__)


@app.route('/')
def score_server():
    try:
        thefile = open("Scores.txt", "r+")
        thescore = int(thefile.read())
        thefile.close()
        return f"<html>\
                    <head>\
                    <title>Scores Game</title>\
                    </head>\
                    <body>\
                    <h1>The score is <div id='score'> {thescore} </div></h1>\
                    </body>\
                    </html>\
                    "
    except Exception as ERROR:
        return f"<html>\
                <head>\
                <title>Scores Game</title>\
                </head>\
                <body>\
                <h1> <div id='score' style=color:red> {ERROR} </div></h1>\
                </body>\
                </html>\
                "


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True, port=8080)
