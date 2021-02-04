import sys
sys.path.append(".")

from sqlalchemy.orm.exc import UnmappedInstanceError
from dao.category_dao import CategoryDao
from models.category import Category
import pytest


class TestCategoryDao:
    @pytest.fixture
    def create_instance(self):
        cat = Category('Uma categoria', 'Uma descrição')
        return cat

    def test_instance(self):
        cat_dao = CategoryDao()
        assert isinstance(cat_dao, CategoryDao)

    def test_save(self, create_instance):
        cat_saved = CategoryDao().save(create_instance)

        assert cat_saved.id_ is not None
        CategoryDao().delete(cat_saved)

    def test_not_save(self):
        with pytest.raises(UnmappedInstanceError):
            cat_saved = CategoryDao().save('category')

    def test_read_by_id(self, create_instance):
        cat_saved = CategoryDao().save(create_instance)
        cat_read = CategoryDao().read_by_id(cat_saved.id_)

        assert isinstance(cat_read, Category)
        CategoryDao().delete(cat_saved)

    def test_not_read_by_id(self):
        with pytest.raises(TypeError):
            cat_read = CategoryDao().read_by_id('cat_saved.id_')

    def test_read_all(self):
        cat_read = CategoryDao().read_all()

        assert isinstance(cat_read, list)

    def test_delete(self, create_instance):
        cat_saved = CategoryDao().save(create_instance)
        cat_read = CategoryDao().read_by_id(cat_saved.id_)
        CategoryDao().delete(cat_read)
        cat_read = CategoryDao().read_by_id(cat_saved.id_)

        assert cat_read is None

    def test_not_delete(self):
        with pytest.raises(UnmappedInstanceError):
            CategoryDao().delete('cat_read')
