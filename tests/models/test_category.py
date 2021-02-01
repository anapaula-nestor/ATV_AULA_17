import sys

sys.path.append(".")

from models.category import Category
import pytest


@pytest.mark.parametrize("name, description", [
    ("Valid name", 'Valid description'),
    ("name" * 10, 'Description' * 5),
    ("Valid name", '')
])
def test_category_instance(name, description):
    name = 'Valid Name'
    description = 'Valid description'
    category = Category(name, description)
    assert isinstance(category, Category)


@pytest.mark.parametrize("name, description", [
    ("Valid name", 'Valid description'),
    ("name" * 10, 'Description' * 5),
    ("Valid name", '')
])
def test_compare_column_model(name, description):
    category = Category(name, description)
    assert category.name == name
    assert category.description == description


@pytest.mark.parametrize("name, description", [
    (1, 'Valid description'),
    ("name" * 10, 5),
    ("Valid name", None)
])
def test_category_args_str(name, description):
    with pytest.raises(TypeError):
        category = Category(name, description)


@pytest.mark.parametrize("name, description", [
    ('Valid name' * 100, 'Valid description'),
    ("Valid name", 'Valid_description' * 100),
])
def test_category_args_max_len(name, description):
    with pytest.raises(ValueError):
        category = Category(name, description)


@pytest.mark.parametrize("name, description", [
    ('', 'Valid description'),
    ("    " * 10, 'Valid_description'),
])
def test_category_name_min_len(name, description):
    with pytest.raises(ValueError):
        category = Category(name, description)
