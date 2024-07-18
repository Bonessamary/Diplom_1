from unittest.mock import Mock
import pytest
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE
from helpers import *

@pytest.fixture(scope='function')
def mock_bun():
    mock_bun = Mock()
    mock_bun.name = bun_name_for_mock
    mock_bun.price = bun_price_for_mock
    return mock_bun

@pytest.fixture(scope='function')
def mock_ingredient():
    mock_ingredient = Mock()
    mock_ingredient.type = INGREDIENT_TYPE_SAUCE
    mock_ingredient.name = bun_name_for_mock
    mock_ingredient.price = ingredient_price_for_mock
    return mock_ingredient

