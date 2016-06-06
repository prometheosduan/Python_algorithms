import random
import string

goal = "methinks it is like a weasel"


def generator():
    sentenceGen = ""
    for x in range(len(goal)):
        sentenceGen += random.choice(string.ascii_lowercase + " ")
    return sentenceGen


def checker(sentenceCheck):
    score = 0
    for x in range(len(goal)):
        if goal[x] == sentenceCheck[x]:
            score += 1
    return score, sentenceCheck


def run():
    score = 0
    times = 0
    scoreBiggest = score
    tupBiggest = None
    while score < len(goal):
        tup = checker(generator())
        score = tup[0]
        if score > scoreBiggest:
            scoreBiggest = score
            tupBiggest = tup
        times += 1
        if times % 1000 == 0:
            print(tupBiggest[1])
    print(times)


if __name__ == "__main__":
    run()
