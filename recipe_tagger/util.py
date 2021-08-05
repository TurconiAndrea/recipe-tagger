"""
Module containing all the support method of the package.
"""

import re

from stop_words import get_stop_words
from textblob import Word

__other_words = {
    "it": [
        "gr",
        "g",
        "freschi",
        "fresche",
        "fresco",
        "fresca",
        "navel",
        "rubis",
        "uht",
        "galbusera",
        "igp",
        "dalfour",
        "vasetto",
        "barattolo",
        "vetro",
        "biologico",
        "biologica",
        "allevate",
        "terra",
        "italia",
        "cat",
        "sardegna",
        "it",
        "granarolo",
        "accadì",
        "william's",
        "artigianale",
        "d'italia",
        "az",
        "luganica",
        "agricola",
        "verga",
        "ml",
        "vaschetta",
        "gusti",
        "gusto",
        "spalmabile",
        "molle",
        "simile",
        "cavalieri",
        "classico",
        "circa",
        "xg",
        "bio",
        "contiene",
        "o'henry",
        "large",
        "medium",
        "small",
        "orange",
        "ferrero",
        "italiano",
        "pronto",
        "consumo",
        "milano",
        "pettinicchio",
        "wagyu",
        "campana",
        "palieri",
        "trentino",
        "st",
        "rapsodia",
        "petti",
        "parzialmente",
        "scremato",
        "cucina",
        "essicato",
        "siciliano",
        "dop",
        "naturale",
        "regina",
        "aperta",
        "parma",
        "affettato",
        "montare",
        "adulto",
        "julienne",
        "fili",
        "extra",
        "d",
        "krumiro",
        "pezzi",
        "spremere",
        "succo",
        "romano",
        "datterini",
        "sungold",
        "croccante",
        "fatto",
        "fatti",
        "bastoncini",
        "lavati",
        "mondati",
        "vergine",
        "baffo",
        "verde",
        "nero",
        "giallo",
        "azzurro",
        "caldo",
        "rosso",
        "rossa",
        "fettina",
        "panata",
        "asciutta",
        "asciutto",
        "tenero",
        "pronti",
        "consumo",
        "italia",
        "formia",
        "lt",
        "composta",
        "dalfour",
        "origine",
        "cuore",
        "spagna",
        "libano",
        "gran bretagna",
        "small",
        "cubettate",
        "preparato",
        "surgelati",
        "baffo",
        "panatura",
        "panato",
        "punta",
        "anca",
        "stagionato",
        "stagionata",
        "scaglie",
        "affumicata",
        "affumicato",
        "cubettato",
        "tritata",
        "tritato",
        "grattuggiato",
        "galline",
        "aperto",
        "antibiotici",
        "madras",
        "vaccina",
        "mezza",
        "luna",
        "pronta" "fette",
        "mix",
        "mascognaz",
        "cubetti",
        "bocconcini",
        "taggiasche",
        "rondelle",
        "tondo",
        "cotti",
        "forno",
        "pelle",
        "pinne",
        "gialle",
        "coltello",
        "eviscerato",
        "d'anca",
        "rosette",
        "fette",
        "altamura",
        "essicato",
        "petit",
        "royal",
        "summer",
        "bianco",
        "cubettata",
        "confettura",
        "%",
        "frutta",
        "mondate",
        "fettine",
        "cubetti",
    ],
    "en": [
        "crushed",
        "crumbles",
        "ground",
        "minced",
        "powder",
        "chopped",
        "sliced",
        "teaspoon",
        "tablespoon",
        "fluid",
        "ounce",
        "gill",
        "cup",
        "pint",
        "quart",
        "gallon",
        "ml",
        "l",
        "dl",
        "pound",
        "mg",
        "g",
        "kg",
        "mm",
        "cm",
        "m",
        "inch",
        "clove",
        "red",
        "bunch",
        "glass",
        "glasses",
        "fresh",
        "chopped",
        "a",
        "red",
        "bunch",
        "and",
        "or",
        "leaf",
        "chilli",
        "large",
        "extra",
        "sprig",
        "ground",
        "handful",
        "free",
        "small",
        "virgin",
        "range",
        "from",
        "dried",
        "sustainable",
        "black",
        "peeled",
        "higher",
        "welfare",
        "seed",
        "for",
        "finely",
        "freshly",
        "sea",
        "quality",
        "white",
        "ripe",
        "few",
        "piece",
        "source",
        "to",
        "organic",
        "flat",
        "smoked",
        "ginger",
        "sliced",
        "green",
        "picked",
        "the",
        "stick",
        "plain",
        "plus",
        "mixed",
        "your",
        "optional",
        "serve",
        "unsalted",
        "baby",
        "fat",
        "ask",
        "natural",
        "skin",
        "roughly",
        "into",
        "such",
        "cut",
        "good",
        "brown",
        "grated",
        "trimmed",
        "yellow",
        "dusting",
        "knob",
        "frozen",
        "on",
        "deseeded",
        "low",
        "runny",
        "balsamic",
        "cooked",
        "streaky",
        "rasher",
        "zest",
        "pin",
        "breadcrumb",
        "halved",
        "grating",
        "stalk",
        "light",
        "tinned",
        "dry",
        "soft",
        "rocket",
        "bone",
        "colour",
        "washed",
        "skinless",
        "leftover",
        "splash",
        "removed",
        "dijon",
        "thick",
        "big",
        "hot",
        "drained",
        "sized",
        "watercress",
        "fishmonger",
        "english",
        "dill",
        "raw",
        "worcestershire",
        "flake",
        "tbsp",
        "leg",
        "pine",
        "wild",
        "if",
        "fine",
        "herb",
        "shoulder",
        "cube",
        "dressing",
        "with",
        "chunk",
        "spice",
        "thumb",
        "garam",
        "new",
        "little",
        "punnet",
        "peppercorn",
        "shelled",
        "other",
        "chopped",
        "taste",
        "can",
        "sauce",
        "water",
        "diced",
        "package",
        "italian",
        "shredded",
        "divided",
        "all",
        "purpose",
        "crushed",
        "juice",
        "more",
        "bell",
        "needed",
        "thinly",
        "boneless",
        "half",
        "cubed",
        "jar",
        "seasoning",
        "extract",
        "sweet",
        "baking",
        "beaten",
        "heavy",
        "seeded",
        "tin",
        "uncooked",
        "crumb",
        "style",
        "thin",
        "coarsely",
        "spring",
        "chili",
        "cornstarch",
        "strip",
        "rinsed",
        "root",
        "quartered",
        "head",
        "softened",
        "container",
        "crumbled",
        "frying",
        "lean",
        "cooking",
        "roasted",
        "warm",
        "whipping",
        "thawed",
        "pitted",
        "sun",
        "kosher",
        "bite",
        "toasted",
        "split",
        "melted",
        "degree",
        "lengthwise",
        "romano",
        "packed",
        "pod",
        "anchovy",
        "rom",
        "prepared",
        "juiced",
        "fluid",
        "floret",
        "room",
        "active",
        "seasoned",
        "mix",
        "deveined",
        "lightly",
        "anise",
        "thai",
        "size",
        "unsweetened",
        "torn",
        "wedge",
        "sour",
        "basmati",
        "marinara",
        "dark",
        "temperature",
        "garnish",
        "bouillon",
        "loaf",
        "shell",
        "reggiano",
        "canola",
        "parmigiano",
        "round",
        "canned",
        "ghee",
        "crust",
        "long",
        "broken",
        "ketchup",
        "bulk",
        "cleaned",
        "condensed",
        "sherry",
        "provolone",
        "cold",
        "soda",
        "cottage",
        "spray",
        "tamarind",
        "pecorino",
        "shortening",
        "part",
        "bottle",
        "sodium",
        "cocoa",
        "grain",
        "french",
        "roast",
        "stem",
        "link",
        "firm",
        "asafoetida",
        "mild",
        "dash",
        "boiling",
        "chopped",
        "skin off",
        "bone out",
        "from sustrainable sources",
    ],
}


__categories = {
    "it": [
        "gelato",
        "sale",
        "pepe",
        "olio",
        "uova",
    ],
    "en": [
        "ice cream",
        "salt",
        "pepper",
        "oil",
        "eggs",
        "egg",
    ],
}


__adjectives_pattern = {
    "it": "[a-zA-Z]*ata|[a-zA-Z]*ato",
    "en": "[a-zA-Z]*ed|[a-zA-Z]*en",
}


def __get_stop_words(language="it"):
    """
    Get the stop words of a selected language plus a collection of non-ingredient
    words usually associated with food and ingredients.

    :param language: the language of the stopwords.
    :return: a list containing all the stopwords of the language.
    """
    stop_words = get_stop_words(language)
    return stop_words + __other_words[language]


def __strip_numeric(string):
    """
    Remove all the numbers in a string.

    :param string: the string where the numbers must be removed.
    :return: a string without numbers.
    """
    return re.sub(r"\d+", "", string)


def __strip_multiple_whitespaces(string):
    """
    Remove all the multiple spaces in a string.

    :param string: the string where the multiple spaces must be removed.
    :return: a string without multiple spaces.
    """
    return re.sub(" +", " ", string)


def __categorize_words(string, language="it"):
    """
    Categorize a string if it contains one of the words in the
    categories dictionary based on the language. If the string
    doesn't contains any of that words, the string will not be modified.

    :param string: the string that can be categorized.
    :param language: the language of the ingredient and category.
    :return: a categorized string or the same string
    """
    category = __categories[language]
    word_list = string.split()
    intersection = list(set(word_list) & set(category))
    return intersection[0] if intersection else string


def __remove_stopwords(string, language="it"):
    """
    Remove all the stopwords inside the provided string based on
    the provided language.

    :param string: the string where the stopwords must be removed.
    :param language: the language of the ingredient and stopwords.
    :return: a string without stopwords.
    """
    word_list = string.split()
    removed_list = [
        word for word in word_list if word not in __get_stop_words(language)
    ]
    return " ".join(removed_list)


def __remove_punctuation(string):
    """
    Remove all the punctuation symbols and characters in a string.

    :param string: the string where the punctation characters must be removed.
    :return: a string without punctuation.
    """
    return re.sub("[!@#£$.()/-]", "", string)


def __remove_adjectives(string, language="it"):
    """
    Remove all the adjectives in a string: adjectives are words that
    indicate a characteristic of the ingredient.
    (Words like fresh, frozen, ..., end with the same pattern)

    :param string: the string where the adjectives must be removed.
    :param language: the language of the ingredients and adjectives.
    :return: a string without adjectives.
    """
    return re.sub(__adjectives_pattern[language], "", string)


def process_ingredients(ing, language="it"):
    """
    Process all the ingredients string in order to retrieve only the word
    correspond to the single ingredients, without number, special charachters,
    punctuation, stopwords, adjectives and multiple whitespaces.

    :param ing: the string corresponding to the raw ingredient.
    :param language: the language of the ingredient.
    :return: a string corresponding to the single ingredient.
    """
    if not ing:
        return None
    ing = ing.lower()
    ing = ing.replace('"', "")
    ing = __strip_numeric(ing)
    ing = __remove_punctuation(ing)
    ing = __remove_stopwords(ing, language)
    ing = __remove_adjectives(ing, language)
    ing = __strip_multiple_whitespaces(ing)
    ing = __categorize_words(ing, language)
    return ing.strip()
