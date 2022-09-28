#! /usr/bin/env python3
# coding : utf-8

from sys import argv
import re


class BadInputException(ValueError):
    """Raised when a given input does not fulfill the specification"""
    pass


class AdnException(ValueError):
    """Raised when a given input does not fulfill the specification"""
    pass


def f_adn(code):
    """
    This function verify if a string value is an DNA sequence or not and
    return the string in upper case

        Parameters:
            code(string):the DNA code to verify

        Raises:
            BadInputException: if the input isn't a string
            AdnException: if the input not correspond to a DNA sequence

        Returns:
            (str): the DNA sequence in upper case
    """
    try:
        if len(code) > 2000:
            raise BadInputException()
        code = code.upper()
        if "t" or "T" in code:
            code = code.replace("t", "U")
            code = code.replace("T", "U")
    except ValueError:
        raise BadInputException()
    return code.strip()


def main(line: str):
    line = line.strip()
    if not len(line) != 0:
        raise BadInputException()
    for i in line:
        if i.upper() not in ["A", "C", "G", "T"]:
            raise AdnException()

    try:
        print(f_adn(line))
    except ValueError:
        raise AdnException()
    ###

    ### Frontal function call and exceptions management

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
            except AdnException:
                print("NOT AN ADN SEQUENCE")
    ###
    print("\r")
