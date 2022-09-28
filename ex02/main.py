#! /usr/bin/env python3
# coding : utf-8

from sys import argv
import re


class BadInputException(ValueError):
    """Raised when a given input does not fulfill the specification"""
    pass

class TooLongStringException(ValueError):
    """Raised when a given input does not fulfill the specification"""
    pass

def alpha(wordlist):
    """
    Return the first string value in the alphabetic order

        Parameters:
            wordlist(list):list of strings values

        Raises:
            BadInputException: if the value is not a ASCII string ([:alpha:]+) NOR the list doesn't contain more than two values

        Returns:
            the first string value in the alphabetic order
    """
    for word in wordlist:
        if len(word) > 16:
            raise TooLongStringException()
    try:
        try:
            wordlist.sort()
        except ValueError:
            raise BadInputException()
        first_word = wordlist[0]
        index = 0
        for word in wordlist:
            if first_word.casefold() == word.casefold():
                if index < wordlist.index(word):
                    index = wordlist.index(word)
        first_word = wordlist[index]
    except ValueError:
        raise BadInputException()
    return first_word


def main(line: str):
    ### Line parsing and BAD INPUT checking
    wordlist = line.split(" ")
    if len(wordlist) > 1:
        for word in wordlist:
            if not re.match("[a-zA-Z]+", word):
                raise BadInputException()
    else:
        raise BadInputException()
    ###

    ### Frontal function call and exceptions management
    try:
        print(alpha(wordlist))
    except TooLongStringException:
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
    ###
    print("\r")
