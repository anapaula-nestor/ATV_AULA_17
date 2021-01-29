import sys

sys.path.append(".")

from models.category import Category


def test_compare_column_model():
    name = 'Category'
    description = 'Description'

    category = Category(name, description)
    assert category.name == name
    assert category.description == description


def test_compare_type_column_model():
    name = 'Category'
    description = 'Description'

    category = Category(name, description)
    assert type(category.name) == str
    assert type(category.description) == str


def test_compare_isinstance():
    name = 'Category'
    description = 'Description'

    category = Category(name, description)
    assert isinstance(category, Category)


def test_has_attribute():
    name = 'Category'
    description = 'Description'

    category = Category(name, description)
    assert hasattr(category, 'name')
    assert hasattr(category, 'description')


def test_none_name_should_return_valueError():
    try:
        Category(None, 'desc')
        raise NotImplementedError("Error not defined")
    except Exception as e:
        assert isinstance(e, ValueError)


def test_none_description_should_return_valueError():
    try:
        Category('name', None)
        raise NotImplementedError("Error not defined")
    except Exception as e:
        assert isinstance(e, ValueError)


def test_not_str_description_should_return_TypeError():
    try:
        Category('name', 1)
        raise NotImplementedError("Error not defined")
    except Exception as e:
        assert isinstance(e, TypeError)


def test_not_str_name_should_return_TypeError():
    try:
        Category(2, '1')
        raise NotImplementedError("Error not defined")
    except Exception as e:
        assert isinstance(e, TypeError)


def test_len_less_200():
    try:
        Category('a' * 300, '1')
        raise NotImplementedError("Error not defined")
    except Exception as e:
        assert isinstance(e, ValueError)


def test_len_less_400():
    try:
        Category('a', 'b' * 600)
        raise NotImplementedError("Error not defined")
    except Exception as e:
        assert isinstance(e, ValueError)
