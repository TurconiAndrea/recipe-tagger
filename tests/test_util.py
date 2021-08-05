"""
Module containg all the tests provided for the util module. 
"""

import pytest

from recipe_tagger import util


# @pytest.mark.skip()
def test_process_ingredient():
    """
    Test for process_ingredient method.
    Test is passed only if the provided ingredient is processed correctly.
    """
    assert (
        util.process_ingredients("farm eggs without antibiotics", language="en")
        == "eggs"
    )
    assert util.process_ingredients("frozen tomatoes", language="en") == "tomatoes"
