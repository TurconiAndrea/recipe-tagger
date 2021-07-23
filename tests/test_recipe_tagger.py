import pytest

from recipe_tagger import recipe_tagger

@pytest.mark.skip()
def test_lemmatize_word():
    assert recipe_tagger.lemmatize_word('aubergines') == 'aubergine'
    assert recipe_tagger.lemmatize_word('legumes') == 'legume'

@pytest.mark.skip()
def test_is_ingredient_vegan():
    assert recipe_tagger.is_ingredient_vegan('apple') == True
    assert recipe_tagger.is_ingredient_vegan('chicken') == False

@pytest.mark.skip()
def test_is_recipe_vegan():
    assert recipe_tagger.is_recipe_vegan(['apple', 'chicken']) == False
    assert recipe_tagger.is_recipe_vegan(['apple', 'pear']) == True

@pytest.mark.skip()
def test_search_ingredient_hypernyms():
    assert recipe_tagger.search_ingredient_hypernyms('pear') == 'fruit'
    assert recipe_tagger.search_ingredient_hypernyms('chicken') == 'meat'
    assert recipe_tagger.search_ingredient_hypernyms('tomato') == 'vegetable'
    assert recipe_tagger.search_ingredient_hypernyms('lemon') == 'fruit'
    assert recipe_tagger.search_ingredient_hypernyms('egg') == 'egg'

@pytest.mark.skip()
def test_search_ingredient_class():
    assert 'fruit' in recipe_tagger.search_ingredient_class('apple')
    assert 'meat' in recipe_tagger.search_ingredient_class('chicken')

#@pytest.mark.skip()
def test_get_ingredient_class():
    assert recipe_tagger.get_ingredient_class('aubergine') == 'vegetable'
    assert recipe_tagger.get_ingredient_class('apple') == 'fruit'
    assert recipe_tagger.get_ingredient_class('chicken') == 'meat'
    assert recipe_tagger.get_ingredient_class('cattle') == 'meat'
    assert recipe_tagger.get_ingredient_class('milk') == 'dairy'

@pytest.mark.skip()
def test_get_recipe_class_percentage():
    assert recipe_tagger.get_recipe_class_percentage(['chicken', 'sausage', 'apple']) == [('meat', '66.67%'), ('fruit', '33.33%')]

@pytest.mark.skip()
def test_get_recipe_tags():
    assert recipe_tagger.get_recipe_tags(['sage']) == []
    assert recipe_tagger.get_recipe_tags(['aubergine']) == ['vegetable']
    assert 'fruit' in recipe_tagger.get_recipe_tags(['pear', 'apple', 'aubergine'])
    assert all(ing in ['staple', 'vegetable'] for ing in recipe_tagger.get_recipe_tags(['bread', 'tomatoes']))
    assert all(ing in ['meat', 'fruit'] for ing in recipe_tagger.get_recipe_tags(['chicken', 'sausage', 'apple']))
