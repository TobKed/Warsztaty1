#!/usr/bin/python3
from random import sample

LOTTO_NUMBERS = sample(range(1, 50), 6)
# LOTTO_NUMBERS = [1, 2, 3, 4, 5, 6]


def validate_input(numbers):
    numbers = numbers.split(" ")
    if not all(x.isdigit() for x in numbers):
        print("input contain non digit characters")
        return
    elif len(numbers) != 6:
        print("you haven't entered six numbers!")
        return False
    elif len(numbers) != len(set(numbers)):
        print("numbers repeat!")
        return False
    elif not all(True if 1<=int(x)<=49 else False for x in numbers):
        print("at least one number is outside range")
        return False
    else:
        return True


def ask_for_numbers():

    while True:
        user_numbers = input("give six non repeating numbers in range 1 - 49:\n")
        if validate_input(user_numbers):
            return sorted([int(x) for x in user_numbers.split(" ")])


def validate_lotto(user, lotto):
    user = set(user)
    lotto = set(lotto)
    match = user & lotto
    matches = len(match)
    if matches >= 3:
        print(f"you have guessed {matches} numbers: {sorted(list(match))}")
    else:
        print("poor result")


if __name__ == '__main__':
    user_numbers = ask_for_numbers()
    print("lotto numbers:\t", LOTTO_NUMBERS)
    print("user numbers:\t", user_numbers)
    validate_lotto(user_numbers, LOTTO_NUMBERS)
