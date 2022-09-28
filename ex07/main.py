#! /usr/bin/env python3
# coding : utf-8

from sys import argv
import re


class BadInputException(ValueError):
    """Raised when a given input does not fulfill the specification"""
    pass


def f_ipsum_sort(line: str):
    """
    This fonction count and sort (in alphabetic order) specifies words in a text

        Parameters:
            line(str):the text input

        Raises:
            BadInputException: if the input isn't a string chain

        Returns:
            string_return(str):the list of words in alphabetic order with the frequency of appareances of each word
    """
    if len(line) > 500:
        raise BadInputException()
    else:
        words = line.split(" ")
        dico_words = {}
        for word in words:
            num = words.count(word.lower())
            dico_words[word] = num
            del word
        string_return = ""
        for k in sorted(dico_words.keys()):
            string_return += "{key}:{value},".format(key=k, value=dico_words[k])
    return string_return.rstrip(",")


def main(line: str):
    ### Line parsing and BAD INPUT checking
    if not re.match(r"^[a-zA-Z ]+$", line):
        raise BadInputException()
    if not len(line) != 0:
        raise BadInputException()
    line = line.lower()
    ###

    ### Frontal function call and exceptions management
    print(f_ipsum_sort(line))

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
