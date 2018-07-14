#!/usr/bin/python3
from random import randint


RANDOM_NUMBER = randint(1, 100)

def guess_number():
    while True:
        try:
            strike = int(input('guess number between 1-100: '))
        except:
            print("it's not a natural number!")
            continue
        if strike > RANDOM_NUMBER:
            print("too much!")
        elif strike < RANDOM_NUMBER:
            print("not enough!")
        elif strike == RANDOM_NUMBER:
            print(strike, "got it !!!")
            break


if __name__ == '__main__':
    guess_number()
