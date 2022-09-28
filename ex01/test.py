#!/usr/bin/env python3
# coding : utf-8

import pytest
from main import simplify, TooLongFloatException


def testSimplify():
    ### Nominal Cases
    #assert simplify(17) == 17
    #assert simplify(38345.6789098765452) == 3.834568e+04
    #assert simplify(.13687846589465132) == 1.368785e-01

    with pytest.raises(TooLongFloatException):
        simplify(1201368784658946513213687846589465132136878465.8 * 1000000000000000000000000000000000000000000000000000000000000e+300)
    ###

