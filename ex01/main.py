#! /usr/bin/env python3
# coding : utf-8

from sys import argv
import re


class BadInputException(ValueError):
    """Raised when a given input does not fulfill the specification"""
    pass


class TooLongFloatException(ValueError):
    """Raised when a given input does not fulfill the specification"""
    pass


def simplify(number):
    """
    Compact an integer or a float with the shortest number of caracters

        Parameters:
            number(int or float): number choose by the user

        Raises:
            BadInputException:if paramater is not an integer or a float

        Returns:
            A classic or scientifique format number depending on its length
    """

    if -1.7976931348623157e-308 <= number <= 1.7976931348623157e+308:
        val = number
        val_sc = format(val, '.6e')
        if len(str(val)) < len(str(val_sc)):
            val_return = val
        elif len(str(val)) > len(str(val_sc)):
            val_return = val_sc
        else:
            val_return = val
    else:
        raise TooLongFloatException()

    return val_return


def main(line: str):
    ### Line parsing and BAD INPUT checking
    try:
        # Convert it into integer
        val = int(line)
        try:
            print(simplify(val))
        except TooLongFloatException:
            print("TOO LONG FLOAT")
    except ValueError:
        try:
            # Convert it into float
            val = float(line)
            try:
                print(simplify(val))
            except TooLongFloatException:
                print("TOO LONG FLOAT")
        except ValueError:
            # Error
            raise BadInputException()

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
    print("\r")
    ###
