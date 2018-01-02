import random

def foodChoice(answerNumber):
    if answerNumber == 1:
        return 'You will eat a pasta dish!'
    elif answerNumber == 2:
        return 'You will eat a cheesy pizza!'
    elif answerNumber == 3:
        return 'You will enjoy a nice medium rare steak!'
    elif answerNumber == 4:
        return 'You will eat a delicious, filling sandwich!'
    elif answerNumber == 5:
        return 'You will eat a grilled chicken dish!'
    elif answerNumber == 6:
        return 'Your meal is Asian noodles with dumplings!'
    elif answerNumber == 7:
        return 'A burger with a side of fries is in your future!'

r = random.randint(1,7)
selection = foodChoice(r)
print(selection)
