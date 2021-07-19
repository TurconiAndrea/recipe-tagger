from setuptools import find_packages, setup

setup(
    name='recipe-tagger',
    packages=find_packages(include=['recipe_tagger']),
    version='0.1.0',
    description='A library for tagging and classify recipes',
    author='Andrea Turconi',
    license='MIT',
    install_requires=['wikipedia', 'PyDictionary', 'textblob', 'pyfood', 'unidecode'],
    test_suite='tests',
    include_package_data=True,
    package_data={'': ['data/*.npy']},
)