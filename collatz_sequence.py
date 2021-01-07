import math
import sys


def collatz(number):
    if math.remainder(number, 2) == 0:
        result = number//2
    else:
        result = 3 * number + 1
    print(result)
    return result


def main_call():
    print(" Hi pal, this is the collatz sequence ".center(50, '-'))
    print("Type in a number please: ")
    try:
        number = int(input())
        result = collatz(number)
        while result != 1:
            result = collatz(result)
    except ValueError:
        print('Please type an integer value')


main_call()
