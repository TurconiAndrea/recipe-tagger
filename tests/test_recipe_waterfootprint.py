"""
Module containg all the tests provided for the recipe water footprint module. 
"""

import pytest

from recipe_tagger import recipe_waterfootprint as wf


# @pytest.mark.skip()
def test_get_ingredient_waterfootprint():
    """
    Test for get_ingredient_waterfootprint method.
    Test is passed only if the water footprint of provided ingredient is correct.
    """
    assert wf.get_ingredient_waterfootprint("tomato", 20, language="en") == 4.28
    assert wf.get_ingredient_waterfootprint("apple", 20, language="en") == 16.44
    assert wf.get_ingredient_waterfootprint("cucumber", 20, language="en") == 7.06
    assert wf.get_ingredient_waterfootprint("chicken", 20, language="en") == 86.5
