from praktikum.bun import Bun
import data

class TestBun:

    # Проверка названия булочки
    def test_get_name_bun(self):
        bun = Bun(data.BUN_NAME, data.BUN_PRICE)
        assert bun.get_name() == data.BUN_NAME

    # Проверка цены булочки
    def test_get_price_bun(self):
        bun = Bun(data.BUN_NAME, data.BUN_PRICE)
        assert bun.get_price() == data.BUN_PRICE