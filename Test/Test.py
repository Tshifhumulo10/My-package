from Mypackage import mymodule

def test_Top_n():
    """Make sure Top_n works correctly"""

    assert mymodule.Top_n([8,9,2,5,7,6], 5), 'incorrect'
    assert mymodule.Top_n([20,7,18,7,6], 5), 'incorrect'
    assert mymodule.Top_n([8,84,100,100,7,6], 5), 'incorrect'
    
