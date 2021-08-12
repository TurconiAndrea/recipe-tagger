"""
Module containing all the methods in order to compute the water footprint of an ingredient or recipe. 
"""

import numpy as np
from nltk.corpus.reader import toolbox

from .foodcategory import FoodCategoryWaterFootprint
from .recipe_tagger import get_ingredient_class
from .util import get_embedding, process_ingredients

waterfootprint_embedding_paths = {"en": "data/ingredient_waterfootprint_en.npy"}


def __calculate_waterfootprint(wf_ing, quantity):
    """
    Calculate the right water footprint of a ingredient from its
    (l/kg) water footprint and the quantity provided (in gr).

    :param wf_ing: the water footprint of the ingredient.
    :param quantity: the quantity of the ingredient.
    :return: the water footprint calcuated on the quantity.
    """
    return (wf_ing * quantity) / 1000


def __get_default_waterfootprint(ingredient, language="en"):
    """
    Get the defualt water footprint of a food category. The recipe tagger
    module is used to predict the class of the ingredient.

    :param ingredient: the ingredient to be classified.
    :param language: the language of the ingredient.
    :return: the defualt water footprint of the predicted category.
    """
    ing_class = get_ingredient_class(ingredient, language)
    return FoodCategoryWaterFootprint[ing_class].value


def get_ingredient_waterfootprint(ingredient, quantity, language="en"):
    """
    Get the water footprint of the provided ingredient based on the quantity.
    If the ingredient is not found in the embedding, the recipe tagger module is
    used to search the category of the ingredient and retrieve the footprint based
    on that.

    :param ingredient: the name of the ingredient.
    :param quantity: the quantity of ingredient to calculate water footprint. (in gr)
    :param language: the language of the ingredient.
    :return: the water footprint of the provided ingredient.
    """
    wf_embedding = get_embedding(waterfootprint_embedding_paths[language])
    ingredient = process_ingredients(ingredient, language=language)
    ingredient_wf = (
        int(wf_embedding[ingredient])
        if ingredient in wf_embedding
        else __get_default_waterfootprint(ingredient, language)
    )
    return __calculate_waterfootprint(ingredient_wf, quantity)


def get_recipe_waterfootprint(ingredients, quantities, language="en"):
    """

    :param ingredients: a list containing all the ingredients of the recipe
    :param quanities: a list containing all the quantiteis of the recipe ingredients
    :param language: the language of the ingredients.
    :return: an integer representing the water footprint of the recipe
    """
    # TODO: check on quantites if they are provided in gr
    total_wf = 0
    for i in range(len(ingredients)):
        total_wf = total_wf + get_ingredient_waterfootprint(
            ingredients[i], quantities[i], language
        )
    return total_wf
