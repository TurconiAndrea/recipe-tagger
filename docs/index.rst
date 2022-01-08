.. recipe tagger documentation master file, created by
   sphinx-quickstart on Sat Jan  8 18:12:35 2022.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Recipe Tagger's documentation!
=========================================

This package provides a classification, a tagging system and a water footprint calculator for ingredients and recipes.
The functioning of the package is based on a dataset containing more than 700 ingredients mapped with their own class and water footprint. If a provided ingredient is not mapped into the dataset, the library search for it on wikipedia pages, into the dictionary and into NLTK Wordnet to find the best possible class. The water footprint is computed based on its ingredients. Every ingredient has a water footprint, measured in l/kg.

An ingredient could be classified in one of the following class: Vegetable, Fruit, Legume, Meat, Egg, Diary, Staple,
Condiment, Nut, Seafood, Snack, Mushroom, Dessert, Beverage.

A recipe is tagged based on its ingredients class. The library also provides a function to get the class percentage of recipe ingredients.

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
