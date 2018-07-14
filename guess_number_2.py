#!/usr/bin/python3


def guess_number():
    min = 0
    max = 1001
    counter = 0
    while True:
        guess = int((max-min) / 2) + min
        counter += 1
        user_input = input(f"I guess: {guess} \t 1: too much 2: not enough 3: got it!\n")
        if user_input == "3":
            print(f"I guessed! It was {guess}!. It took me {counter} tries!")
            break
        elif user_input == "1":
            max = guess
        elif user_input == "2":
            min = guess
        else:
            print("Come on! Don't cheat!")
            counter -= 1


if __name__ == '__main__':
    print("think number between 1 - 1000 and I will guess it in 10 moves !!!")
    guess_number()

