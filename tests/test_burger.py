from praktikum.burger import Burger
from helpers import *
from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE


class TestBurger:

    # Проверка выбора булочки
    def test_set_bun(self, mock_bun):
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

    # Проверка добавления ингредиентов в бургер
    def test_add_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert mock_ingredient in burger.ingredients

    # Проверка удаления ингредиентов из бургера
    def test_remove_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        index = burger.ingredients.index(mock_ingredient)
        burger.remove_ingredient(index)
        assert mock_ingredient not in burger.ingredients

    # Проверка перемещения ингридиентов
    def test_move_ingredient(self, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.add_ingredient(mock_ingredient)
        ingredient = burger.ingredients[0]
        burger.move_ingredient(0, 1)
        assert burger.ingredients[1] == ingredient

    # Проверка получения цены бургера
    def test_get_price_burger(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.set_buns(mock_bun)
        mock_bun.get_price.return_value = bun_price_for_mock
        mock_ingredient.get_price.return_value = ingredient_price_for_mock
        assert burger.get_price() == bun_price_for_mock * 2 + ingredient_price_for_mock

    # Проверка получения рецепта бургера
    def test_get_receipt_burger(self, mock_bun, mock_ingredient):
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.set_buns(mock_bun)
        mock_bun.get_name.return_value = bun_name_for_mock
        mock_bun.get_price.return_value = bun_price_for_mock
        mock_ingredient.get_type.return_value = INGREDIENT_TYPE_SAUCE
        mock_ingredient.get_name.return_value = ingredient_name_for_mock
        mock_ingredient.get_price.return_value = ingredient_price_for_mock
        receipt = f'(==== {bun_name_for_mock} ====)\n' \
              f'= sauce {ingredient_name_for_mock} =\n' \
              f'(==== {bun_name_for_mock} ====)\n' \
              f'\nPrice: {bun_price_for_mock * 2 + ingredient_price_for_mock}'
        assert burger.get_receipt() == receipt