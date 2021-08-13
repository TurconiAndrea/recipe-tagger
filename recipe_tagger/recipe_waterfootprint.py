"""
Module containing all the methods in order to compute the water footprint of an ingredient or recipe. 
"""

import numpy as np
from nltk.corpus.reader import toolbox

from .foodcategory import FoodCategoryWaterFootprint
from .recipe_tagger import get_ingredient_class
from .util import get_embedding, process_ingredients

waterfootprint_embedding_paths = {
    "en": "data/ingredient_waterfootprint_en.npy",
    "it": "data/ingredient_waterfootprint_ita.npy",
}


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


def __get_embedding_trimmed(language="en"):
    """
    Return the embedding of the ingredient without the last letter in order
    to check singular and plurals for different language not singularized
    with the method of the util file.
    :param language: the language of the embedding.
    :return: the embedding where each ingredient is trimmed.
    """
    embedding = get_embedding(waterfootprint_embedding_paths[language])
    values = [v for v in embedding.values()]
    trimmed = [ing[:-1] for ing in embedding.keys()]
    return {trimmed[i]: values[i] for i in range(len(embedding))}


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
    wf_embedding_trimmed = __get_embedding_trimmed(language)
    ingredient = process_ingredients(ingredient, language=language)

    ingredient_wf = 0
    if ingredient in wf_embedding:
        ingredient_wf = int(wf_embedding[ingredient])
    elif ingredient[:-1] in wf_embedding_trimmed:
        ingredient_wf = int(wf_embedding_trimmed[ingredient])
    else:
        ingredient_wf = __get_default_waterfootprint(ingredient, language)
    return __calculate_waterfootprint(ingredient_wf, quantity)


def get_recipe_waterfootprint(ingredients, quantities, language="en"):
    """
    Get the water footprint of a recipe, providing the ingredients and the
    quantities for each ingredient. Params ingredients and quantities must have
    the same length. Quantites are strings containing the values and the unit
    without spaces (10gr).
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
