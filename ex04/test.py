#!/usr/bin/env python3
# coding : utf-8

import pytest
from main import f_adn, BadInputException


def testADN():  # Rename accordingly

    ### Nominal Cases
    assert f_adn("AGGATTC") == "AGGAUUC"
    assert f_adn("ATTTTTGCGT") == "AUUUUUGCGU"
    assert f_adn("AttGCTA") == "AUUGCUA"
    ###

    ### Edge cases and corner cases
    with pytest.raises(BadInputException):
        f_adn("t"*200000)
        f_adn("56")
    ###
