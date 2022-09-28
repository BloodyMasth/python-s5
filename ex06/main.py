#! /usr/bin/env python3
# coding : utf-8

from sys import argv
import re
import csv


class BadInputException(ValueError):
    """Raised when a given input does not fulfill the specification"""
    pass


def f_compteur(val_n, val_m, list_columns, path):
    """
    This fonction return the amount of values in specifies columns in a csv file

        Parameters:
            val_n(int):the begining value of the intervale of lines
            val_m(int):the end value of the intervale of lines
            list_columns(list):list of columns names
            path(string):the UNIX path to the csv file

        Raises:
            BadInputException:if the input doesn't match with the expected values

        Returns:
            sum(int): the sum of all value in the intervale
    """
    try:
        with open(path, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',')
            line_count = 0
            somme = 0
            index_list = []
            for row in spamreader:
                if line_count == 0:
                    title = row
                    for i in range(len(list_columns)):
                        index_list.append(title.index(list_columns[i]))
                if int(val_n) < line_count <= int(val_m) + 1:
                    colone = 1
                    for i in index_list:
                        colone = colone * float(row[i])
                    somme += colone
                line_count += 1
    except ValueError:
        raise BadInputException()
    return somme


def main(line: str):
    ### Line parsing and BAD INPUT checking
    line_split = line.split(" ")
    path = ""
    if not line_split[0].isdigit() or not line_split[1].isdigit():
        raise BadInputException()
    else:
        val_n = int(line_split[0])
        val_m = int(line_split[1])

    path_passed = False
    begin_path = 0
    for i in line_split:
        if path_passed:
            path += " " + i
        if '/' in i:
            begin_path = line_split.index(i)
            path += i
            path_passed = True
    del line_split[begin_path:]

    path = path.strip()
    try:
        open(path)
    except ValueError:
        raise BadInputException()

    row_counter = -1
    for line in open(path):
        row_counter += 1
    if int(val_n) < 0:
        raise BadInputException()
    elif not int(val_m) < row_counter:
        raise BadInputException()

    list_columns = []
    for i in range(2, len(line_split)):
        if not re.match(r"^[a-zA-Z]+$", line_split[i]):
            raise BadInputException()
        else:
            list_columns.append(line_split[i])



    ###

    ### Frontal function call and exceptions management
    try:
        print(f_compteur(val_n, val_m, list_columns, path))
    except ValueError:
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
        print("")
    ###
