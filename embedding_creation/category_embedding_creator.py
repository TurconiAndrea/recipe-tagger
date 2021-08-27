import argparse
from enum import Enum
from os import sep

import numpy as np
import pandas as pd
from nltk.stem.snowball import SnowballStemmer

ENGLISH = "english"
ITALIAN = "italian"
ALL = "all"
FOODCATEGORY = "foodcategory"
WATERFOOTPRINT = "waterfootprint"


class FoodCategory(Enum):
    """
    Enum class used to represent the category of ingredients.
    """

    vegetable = 0
    fruit = 1
    legume = 2
    meat = 3
    egg = 4
    dairy = 5
    staple = 6
    condiment = 7
    nut = 8
    seafood = 9
    snack = 10
    mushroom = 11
    dessert = 12
    beverage = 13


food_categories_paths = {
    ENGLISH: "data/food_category_en.csv",
    ITALIAN: "data/food_category_it.csv",
}

food_categories_save = {
    ENGLISH: "../recipe_tagger/data/ingredient_embedding_en.npy",
    ITALIAN: "../recipe_tagger/data/ingredient_embedding_it.npy",
}

water_footprint_paths = {ENGLISH: "data/wf_en.csv", ITALIAN: "data/wf_it.csv"}

water_footprint_save = {
    ENGLISH: "../recipe_tagger/data/ingredient_waterfootprint_en.npy",
    ITALIAN: "../recipe_tagger/data/ingredient_waterfootprint_it.npy",
}


def map_category(type):
    """
    Map the category with the correspondent into the FoodCategory enum.

    :param type: the type of the ingredient.
    :return: the FoodCategory of the ingredient.
    """
    return FoodCategory[type.lower()].value


def get_stemmer(language):
    """
    Intialize the stemmer with the provided language.

    :param language: the language in use for the embedding.
    :return: the stemmer initialized with the provided language.
    """
    return SnowballStemmer(language=language)


def stem_word(word, stemmer):
    """
    Produce the stemming of the provided word.

    :param word: the word to be stemmed.
    :param stemmer: the stemmer.
    :return: the word stemmed.
    """
    word = word.strip()
    return stemmer.stem(word)


def get_data(type=FOODCATEGORY, langauge=ENGLISH):
    """
    Get the csv file for the embedding.

    :param type: the type of the embedding.
    :param language: the language of the embedding.
    :return: a pandas datafram representing the data for the embedding.
    """
    if type == FOODCATEGORY:
        return pd.read_csv(food_categories_paths[langauge], sep=";")
    elif type == WATERFOOTPRINT:
        return pd.read_csv(water_footprint_paths[langauge], sep=";")


def save_embedding(data, type=FOODCATEGORY, language=ENGLISH):
    """
    Save the embedding as a npy format.

    :param data: the data cleaned for the embedding.
    :param type: the type of the embedding.
    :param language: the language of the embedding.
    """
    data = data.to_dict()
    if type == FOODCATEGORY:
        np.save(food_categories_save[language], data["type"])
    elif type == WATERFOOTPRINT:
        np.save(water_footprint_save[language], data["final"])


def generate_category_embedding(language=ENGLISH):
    """
    Generate the food category embedding.

    :param language: the language of the embedding.
    """
    stemmer = get_stemmer(language)
    data = get_data(FOODCATEGORY, language)
    data["ingredient"] = data.apply(lambda x: x["ingredient"].lower(), axis=1)
    data["ingredient"] = data.apply(
        lambda x: stem_word(x["ingredient"], stemmer=stemmer), axis=1
    )
    data["type"] = data.apply(lambda x: map_category(x["type"]), axis=1)
    data.index = data["ingredient"]
    data = data.drop(columns=["ingredient"])
    save_embedding(data, type=FOODCATEGORY, language=language)


def generate_waterfootprint_embedding(language=ENGLISH):
    """
    Generate the water footprint embedding.

    :param language: the language of the embedding.
    """
    stemmer = get_stemmer(language)
    data = get_data(WATERFOOTPRINT, language)
    data["product"] = data.apply(lambda x: x["product"].lower(), axis=1)
    data["product"] = data.apply(
        lambda x: stem_word(x["product"], stemmer=stemmer), axis=1
    )
    data["final"] = list(zip(data["wf (l/kg)"], data["weight"]))
    data.index = data["product"]
    data = data.drop(columns=["product"])
    save_embedding(data, type=WATERFOOTPRINT, language=language)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Script for the creation of the food category and water footprint embedding"
    )
    parser.add_argument(
        "-l",
        action="store",
        dest="language",
        help="-l: Choose the language of the embedding (english or italian)",
    )
    parser.add_argument(
        "-t",
        action="store",
        dest="type",
        help="-t: Choose the type of the embedding (foodcategory or waterfootprint or all)",
    )
    arguments = parser.parse_args()
    type = arguments.type if arguments.type else FOODCATEGORY
    language = arguments.language if arguments.language else ENGLISH

    print(f"=============== Creating {type} embedding ===================")
    print(f"=============== Creating {language} embedding ===============")

    if type == FOODCATEGORY:
        generate_category_embedding(language)
    elif type == WATERFOOTPRINT:
        generate_waterfootprint_embedding(language)
    elif type == ALL:
        generate_category_embedding(language)
        generate_waterfootprint_embedding(language)

    print(f"=============== Done ========================================")
