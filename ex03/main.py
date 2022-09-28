#! /usr/bin/env python3
# coding : utf-8

from sys import argv
import re
from math import *


class BadInputException(ValueError):
    """Raised when a given input does not fulfill the specification"""
    pass


class ArithmeticException(ValueError):
    """Raised when a given input does not fulfill the specification"""
    pass


def sqrt_f(floatA, floatB):
    """
    This fonction takes 2 floats and return the round value of the next calcul :
    sqrt((sin(A)/A)*(sin(B)/B))

        Parameters:
            floatA (float): first value, the A in the formula
            floatB (float): second value, the B in the formula

        Raises:
            ArithmeticException: if the calcul isn't possible

        Returns:
            (float): the result of the calcul or an error
    """
    calcul = 0

    if floatA != 0 and floatB != 0:
        calcul = sqrt((sin(floatA) / floatA) * (sin(floatB) / floatB))
        calcul = round(calcul, 5)
    else:
        raise ArithmeticException()

    return calcul


def main(line: str):
    ### Line parsing and BAD INPUT checking
    try:
        # Convert it into integer
        floatA, floatB = line.split(" ")
        floatA = float(floatA)
        floatB = float(floatB)

    except ValueError:
        raise BadInputException()
    ###

    ### Frontal function call and exceptions management
    try:
        print(sqrt_f(floatA, floatB))
    except ArithmeticException:
        print("ARITHMETIC ERROR")
    ###


if __name__ == "__main__":

    ### Input file reading
    ### One line = one call to main function
    with open(argv[1]) as inputFile:
        for line in inputFile:
            try:
                main(line)
            except BadInputException:
                print("BAD INPUT")


    ###
