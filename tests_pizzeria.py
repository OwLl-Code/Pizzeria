import pizzeria
import pytest

pizza = pizzeria.Pizza()

def test():
    assert pizzeria.Pizza().make_pizza('Margarita', 80) == 'Pizza ready!'
    assert pizzeria.Pizza().make_pizza('Capricciosa', 0) == 'Pizza ready!'
    assert pizzeria.Pizza().make_pizza('Calzone', 20) == 'Pizza ready!'


def test_pizzaError():
    with pytest.raises(pizzeria.PizzaError):
        pizzeria.Pizza().make_pizza('Mrgrta', 80)
    

def test_TNCError():
    with pytest.raises(pizzeria.TooMuchCheeseError):
        pizzeria.Pizza().make_pizza('Capricciosa', 800)
        