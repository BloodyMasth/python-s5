#!/usr/bin/env python3
# coding : utf-8

import pytest
from main import alpha, BadInputException


def testalpha():
    ### Nominal Cases
    assert alpha(["bob", "calice", "pierre"]) == "bob"
    ###

    ### Edge cases and corner cases
    with pytest.raises(BadInputException):
        alpha(["25\@", "calice", "pierre"])
    ###
