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

def f_adn_interator(patern: str, chaine: str) -> str:
    """
    This fonction compare 2 DNA sequences and return the
    number of iterations of a DNA pattern in a given string

        Parameters:
            patern(str):DNA string that we look in the big chain
            chaine(str):DNA string sequence

        Raises:
            BadInputException:if the input values aren't string

        Returns:
            (str):string of numbers of interations

    """
    index_string = 0
    if chaine.count(patern) == 0:
        string_return = "False"
    else:
        string_return = str(chaine.count(patern))
        for i in range(0, chaine.count(patern)):
            string_return += "," + str(chaine.index(patern, index_string))
            index_string += chaine.index(patern, index_string) + 1

    return string_return


def main(line: str):
    ### Line parsing and BAD INPUT checking
    try:
        if not len(line) != 0:
            raise BadInputException()
        patern, chaine = line.split()
    except ValueError:
        raise BadInputException()
    for i in patern:
        if i.upper() not in ["A", "C", "G", "T"]:
            raise AdnException()
    for i in chaine:
        if i.upper() not in ["A", "C", "G", "T"]:
            raise AdnException()
    ###
    try:
        print(f_adn_interator(patern, chaine))
    except ValueError:
        raise BadInputException()


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
        print("")
    ###
