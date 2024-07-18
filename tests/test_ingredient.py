import pytest
import data
from praktikum.ingredient import Ingredient

class TestIngredient:

    # Проверка типа ингредиента
    @pytest.mark.parametrize("ingredient_type, ingredient_name, ingredient_price", data.INGREDIENTS)
    def test_get_type_ingredient(self, ingredient_type, ingredient_name, ingredient_price):
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        assert ingredient.get_type() == ingredient_type

    # Проверка имени ингредиента
    @pytest.mark.parametrize("ingredient_type, ingredient_name, ingredient_price", data.INGREDIENTS)
    def test_get_name_ingredient(self, ingredient_type, ingredient_name, ingredient_price):
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        assert ingredient.get_name() == ingredient_name

    # Проверка цены ингредиента
    @pytest.mark.parametrize("ingredient_type, ingredient_name, ingredient_price", data.INGREDIENTS)
    def test_get_price_ingredient(self, ingredient_type, ingredient_name, ingredient_price):
        ingredient = Ingredient(ingredient_type, ingredient_name, ingredient_price)
        assert ingredient.get_price() == ingredient_price