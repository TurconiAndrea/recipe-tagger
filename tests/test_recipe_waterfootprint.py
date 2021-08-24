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
    assert (
        wf.get_ingredient_waterfootprint("tomato", 20, process=True, language="en")
        == 4.28
    )
    assert (
        wf.get_ingredient_waterfootprint("apple", 20, process=True, language="en")
        == 16.44
    )
    assert (
        wf.get_ingredient_waterfootprint("cucumber", 20, process=True, language="en")
        == 7.06
    )
    assert (
        wf.get_ingredient_waterfootprint("chicken", 20, process=True, language="en")
        == 86.5
    )
    assert (
        wf.get_ingredient_waterfootprint("ombrina", 20, process=True, language="it")
        == 51.8
    )


# @pytest.mark.skip()
def test_get_recipe_waterfootprint():
    """
    Test for get_recipe_waterfootprint method.
    Test if passed only if the calculated water footprint of the recipe is correct.
    """
    assert (
        wf.get_recipe_waterfootprint(
            ["tomato", "apple", "chicken"], ["20gr", "5ml", "1l"], language="en"
        )
        == 4329.28
    )
    assert (
        wf.get_recipe_waterfootprint(
            ["tomato", "apple", "chicken"],
            ["20gr", "5ml", "1l"],
            language="en",
            information=True,
        )
        == (4329.28, {"tomato": 4.28, "apple": 0.0, "chicken": 4325.0})
    )
    assert (
        wf.get_recipe_waterfootprint(
            ["tomato", "apple", "chicken"],
            ["20gr", "2unit", "1l"],
            language="en",
            information=True,
        )
        == (4658.08, {"tomato": 4.28, "apple": 328.8, "chicken": 4325.0})
    )
    assert (
        wf.get_recipe_waterfootprint(
            ["tomato", "apple", "chicken", "mango"],
            ["20gr", "2unit", "1l", "1None"],
            language="en",
            information=True,
        )
        == (4658.08, {"tomato": 4.28, "apple": 328.8, "chicken": 4325.0, "mango": 0.0})
    )
    assert (
        wf.get_recipe_waterfootprint(
            ["pomodori", "mela", "pollo"], ["20gr", "5ml", "1l"], language="it"
        )
        == 4329.28
    )
