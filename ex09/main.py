#! /usr/bin/env python3
# coding : utf-8

from sys import argv
import re


class BadInputException(ValueError):
    """Raised when a given input does not fulfill the specification"""
    pass


def f_search(patern, path):
    """
    This function search all words in a text matching with the input patern

        Parameters:
            patern(str):the patern to match
            path(str):the file path

        Raises:
            BadInputException:if the given path doesn't respect the format

        Returns:
            string_return(str):words who match with the patern in the text order
    """
    string_return = ""
    try:
        with open(path) as file:
            for line in file:
                words = line.split()
                for word in words:
                    if not re.match(r"^[a-zA-Z]*$", word):
                        raise BadInputException()
                    string_split = patern.split("*")
                    count = 0
                    word_to_check = word
                    for i in range(len(string_split)):
                        if string_split[i] in word_to_check:
                            count += 1
                            word_to_check = word_to_check.split(string_split[i])[1]
                    if count == len(string_split):
                        string_return += word.strip() + " "
    except ValueError:
        raise BadInputException()

    return string_return


def main(line: str):
    ### Line parsing and BAD INPUT checking
    line_split = line.split(" ")
    patern = line_split[0]
    path = line_split[1]
    if not re.match(r"^[a-zA-Z\*]+$", patern):
        raise BadInputException()
    print(f_search(patern, path))
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
    ###
