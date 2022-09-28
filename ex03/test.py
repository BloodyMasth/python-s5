#!/usr/bin/env python3
# coding : utf-8

import pytest
from main import sqrt_f, ArithmeticException


def testFonction():
    ### Nominal Cases
    assert sqrt_f(2.1, 3) == 0.13905

    ###

    ### Edge cases and corner cases
    with pytest.raises(ArithmeticException):
        sqrt_f(0, 5)
        sqrt_f(4.7, 0.01)

    ###
