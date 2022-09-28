#!/usr/bin/env python3
#coding : utf-8

import pytest
from main import f_ipsum_sort, BadInputException
 
def testFrontalFunction(): # Rename accordingly
    
    ### Nominal Cases
    assert f_ipsum_sort("poisson pierre caillou rocher roger poisson") == 'caillou:1,pierre:1,poisson:2,rocher:1,roger:1'
    ###
    
    
    ### Edge cases and corner cases
    with pytest.raises(BadInputException):
        f_ipsum_sort("pierre" * 1000)
    ###