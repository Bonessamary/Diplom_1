from random import choice, randrange
from string import ascii_lowercase


bun_name_for_mock = ''.join(choice(ascii_lowercase) for b in range(10))
bun_price_for_mock = randrange(100, 1000)
ingredient_name_for_mock = ''.join(choice(ascii_lowercase) for i in range(10))
ingredient_price_for_mock = randrange(100, 1000)