import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from .factories import BrandFactory, CategoryFactory, ProductFactory

register(CategoryFactory)
register(BrandFactory)
register(ProductFactory)

# Accesing in this manner category_factory
# pytestfixture lets sink with a function : A function which we can then make availible to other tests
# These functions may provide data for testing and another wide range of values taht our test might need


@pytest.fixture
def api_client():
    return APIClient
