#!/usr/bin/env python3
#coding : utf-8

import pytest
from main import f_compteur, BadInputException
 
def testFrontalFunction(): # Rename accordingly
    
    ### Nominal Cases
    assert f_compteur(2, 5, ["price", "quantity"], "./ex06/file.csv") == 476.7
    ###
    
    
    ### Edge cases and corner cases
    with pytest.raises(BadInputException):
        f_compteur(2, 5, ["price", "quanty"], "./ex06/file.csv")
        f_compteur(2, 5, ["price", "quantity", "test"], "./ex06/file.csv")
    ###