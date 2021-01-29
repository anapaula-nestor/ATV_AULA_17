import sys

sys.path.append(".")

from models.category import Category
import pytest


def test_category_instance():
    name = 'Valid Name'
    description = 'Valid description'
    category = Category(name, description)
    assert isinstance(category, Category)


def test_compare_column_model():
    name = 'Category'
    description = 'Description'
    category = Category(name, description)
    assert category.name == name
    assert category.description == description


def test_category_name_str():
    with pytest.raises(TypeError):
        category = Category(1, 'Valid description')


def test_category_name_min_len():
    with pytest.raises(ValueError):
        category = Category('', 'Valid description')


def test_category_name_max_len():
    with pytest.raises(ValueError):
        category = Category('nome' * 100, 'Valid description')


def test_category_description_str():
    with pytest.raises(TypeError):
        category = Category('Valid name', None)


def test_category_description_min_len():
    with pytest.raises(ValueError):
        category = Category('Valid name', '')


def test_category_description_max_len():
    with pytest.raises(ValueError):
        category = Category('Valid name', 'description'*100)
