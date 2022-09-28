#!/usr/bin/env python3
#coding : utf-8

import pytest
from main import f_fizz_buzz, BadInputException
 
def testFrontalFunction(): # Rename accordingly
    
    ### Nominal Cases
    assert f_fizz_buzz([(1, "test"), (2, "test2")], 3) == 'test\ntesttest2\ntest'
    ###
    
    
    ### Edge cases and corner cases
    with pytest.raises(BadInputException):
        f_fizz_buzz([("test", 1), ("test2", 2)], 3)
    ###