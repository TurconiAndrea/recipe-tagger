"""
Setup file for pubblication.
"""


import pathlib

from setuptools import find_packages, setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(
    name="recipe-tagger",
    packages=find_packages(include=["recipe_tagger"]),
    version="0.3.6",
    description="A library for tagging and classify recipes",
    author="Andrea Turconi",
    license="MIT",
    long_description=README,
    long_description_content_type="text/markdown",
    url="https://github.com/TurconiAndrea/recipe-tagger",
    download_url="https://github.com/TurconiAndrea/recipe-tagger/archive/refs/tags/0.3.6.tar.gz",
    keywords=["food", "recipe", "tag", "tagging", "ingredient"],
    install_requires=[
        "wikipedia-api",
        "PyDictionary",
        "textblob",
        "pyfood",
        "unidecode",
        "numpy",
        "nltk",
    ],
    test_suite="tests",
    package_data={"": ["data/*.npy"]},
)
