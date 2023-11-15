import pytest

pytestmark = pytest.mark.django_db


class TestCategoryModel:
    # we can aaa acronym for testing
    # Arrange,action,assert three stages
    def test_str_method(self, category_factory):
        # Arrange
        # Act
        x = category_factory(name="Test")
        # Assert
        assert x.__str__() == "Test"


class TestBrandModel:
    def test_str_method(self, brand_factory):
        test_brand = brand_factory(name="Lokesh")

        assert test_brand.__str__() == "Lokesh"


class TestProductModel:
    def test_str_method(self, product_factory):
        test_product = product_factory()

        assert test_product.__str__() == "Product_4"
