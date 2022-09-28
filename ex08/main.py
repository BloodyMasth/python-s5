#! /usr/bin/env python3
# coding : utf-8

from sys import argv
import re


class BadInputException(ValueError):
    """Raised when a given input does not fulfill the specification"""
    pass


def f_fizz_buzz(tuple_iteration, iteration) -> str:
    """
    This function does an iteration in the given input interval. If the number is divisible by
    the interger associated with fizz, the fonction replace the number by the fizz, same for buzz.
    If the interger of fizz and buzz can divides the number, the fonction return the concatenation of fizz and buzz

        Parameters:
            tuple_interation(tuple):the list of tuple who contain the pair of int fizz and int buzz
            iteration(int):the number of interation

        Raises:
            BadInputException: if the input isn't match with the type expected, if the separator isn't a space

        Returns:
            string_return(str):the fizz and buzz or concatenation values
    """
    try:
        string_return = ""
        iteration += 1
        for i in range(1, iteration):
            fizzbuzz = False
            for j in range(len(tuple_iteration)):
                if i % int(tuple_iteration[j][0]) == 0:
                    string_return += str(tuple_iteration[j][1])
                    fizzbuzz = True
            if not fizzbuzz:
                string_return += str(i) + "\n"
            else:
                string_return += "\n"
    except ValueError:
        raise BadInputException()
    return string_return.strip()


def main(line: str):
    ### Line parsing and BAD INPUT checking
    line_split = line.split(" ")
    iteration = int(line_split.pop())
    tuple_list = []
    if iteration < 1:
        raise BadInputException()
    for i in range(0, len(line_split), 2):
        if re.match(r"^[a-zA-Z]+$", line_split[i + 1]):
            tuple_value = (line_split[i], line_split[i + 1])
            tuple_list.append(tuple_value)
        else:
            raise BadInputException()
    ###

    ### Frontal function call and exceptions management
    print(f_fizz_buzz(tuple_list, iteration))
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
