FROM python:3
WORKDIR /app
COPY MainScores.py Scores.txt /app
CMD python MainScores.py