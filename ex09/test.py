#!/usr/bin/env python3
#coding : utf-8

import pytest
from main import f_search, BadInputException
 
def testFrontalFunction(): # Rename accordingly
    
    ### Nominal Cases
    assert f_search("a*et", "./ex09/file.txt") == 'laoreet nascetur aliquet pharetra '
    ###
    
    
    ### Edge cases and corner cases
    with pytest.raises(BadInputException):
        f_search("a*et", "./ex09/b1t3.txt")
    ###