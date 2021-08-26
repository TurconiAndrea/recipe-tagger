"""
Module containg all the tests provided for the recipe_tagger module. 
"""

import pytest

from recipe_tagger import recipe_tagger


@pytest.mark.skip()
def test_is_ingredient_vegan():
    """
    Test for is_ingredient_vegan method.
    Test is passed only if the provided ingredient is vegan and classified
    vegan or otherwise.
    """
    assert recipe_tagger.is_ingredient_vegan("apple") == True
    assert recipe_tagger.is_ingredient_vegan("chicken") == False


@pytest.mark.skip()
def test_is_recipe_vegan():
    """
    Test for is_recipe_vegan method.
    Test is passed only if the provided recipe is vegan and classified
    vegan or otherwise.
    """
    assert recipe_tagger.is_recipe_vegan(["apple", "chicken"]) == False
    assert recipe_tagger.is_recipe_vegan(["apple", "pear"]) == True


@pytest.mark.skip()
def test_add_ingredient():
    """
    Test for add_ingredient method.
    Test is passed only if the provided ingredient is not into the embedding.
    """
    assert recipe_tagger.add_ingredient("milk", "dairy") == False


@pytest.mark.skip()
def test_search_ingredient_hypernyms():
    """
    Test for search_ingredient_hypernyms method.
    Test is passed only if the provided ingredient is classified correctly
    using its hypernyms.
    """
    assert recipe_tagger.search_ingredient_hypernyms("pear") == "fruit"
    assert recipe_tagger.search_ingredient_hypernyms("chicken") == "meat"
    assert recipe_tagger.search_ingredient_hypernyms("tomato") == "vegetable"
    assert recipe_tagger.search_ingredient_hypernyms("lemon") == "fruit"
    assert recipe_tagger.search_ingredient_hypernyms("egg") == "egg"


@pytest.mark.skip()
def test_search_ingredient_class():
    """
    Test for search_ingredient_class method.
    Test is passed only if the provided ingredient is classified correctly
    using dictionary and wikipedia.
    """
    assert "fruit" in recipe_tagger.search_ingredient_class("apple")
    assert "meat" in recipe_tagger.search_ingredient_class("chicken")


@pytest.mark.skip()
def test_get_ingredient_class():
    """
    Test for get_ingredient_class method.
    Test is passed only if the provided ingredient is classified correctly
    using embedding, dictionary, wikipedia and hypernyms.
    """
    assert recipe_tagger.get_ingredient_class("tomatoes") == "vegetable"
    assert recipe_tagger.get_ingredient_class("aubergine") == "vegetable"
    assert recipe_tagger.get_ingredient_class("apple") == "fruit"
    assert recipe_tagger.get_ingredient_class("chicken") == "meat"
    assert recipe_tagger.get_ingredient_class("cattle") == "meat"
    assert recipe_tagger.get_ingredient_class("milk") == "dairy"
    assert recipe_tagger.get_ingredient_class("porcini") == "mushroom"
    assert recipe_tagger.get_ingredient_class("chips") == "snack"


@pytest.mark.skip()
def test_get_recipe_class_percentage():
    """
    Test for get_recipe_class_percentage method.
    Test is passed only if the provided recipe is classified correctly
    with its class percentage.
    """
    assert recipe_tagger.get_recipe_class_percentage(
        ["chicken", "sausage", "apple"]
    ) == [("meat", "66.67%"), ("fruit", "33.33%")]


@pytest.mark.skip()
def test_get_recipe_tags():
    """
    Test for get_recipe_tags method.
    Test is passed only if the provided recipe is classified correctly.
    This means that all the ingredients of the recipe must be classified correctly.
    """
    assert recipe_tagger.get_recipe_tags(["aubergine"]) == ["vegetable"]
    assert recipe_tagger.get_recipe_tags(["olive oil", "chicken"]) == ["meat"]
    assert "fruit" in recipe_tagger.get_recipe_tags(["pear", "apple", "aubergine"])
    assert all(
        ing in ["staple", "vegetable"]
        for ing in recipe_tagger.get_recipe_tags(["bread", "tomatoes"])
    )
    assert all(
        ing in ["meat", "fruit"]
        for ing in recipe_tagger.get_recipe_tags(["chicken", "sausage", "apple"])
    )
    assert all(
        ing in ["meat", "fruit"]
        for ing in recipe_tagger.get_recipe_tags(
            ["baked chicken", "apple", "crunchy pear"]
        )
    )
    assert all(
        ing in ["meat", "vegetable"]
        for ing in recipe_tagger.get_recipe_tags(["scamone", "carote"], language="it")
    )
