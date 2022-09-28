#!/usr/bin/env python3
# coding : utf-8

import pytest
from main import f_adn_interator


def testFrontalFunction():  # Rename accordingly

    ### Nominal Cases
    assert f_adn_interator("acgt", "aacgtggcatgacgtggataa") == "2,1,11"
    assert f_adn_interator("azerty", " ") == "False"
    ###

    ### Edge cases and corner cases
    ###