import pytest
from src.cart import Cart


def test_add_item():
    cart = Cart()
    cart.add_item("Mouse", 50, 2)

    assert len(cart.items) == 1
    assert cart.calculate_total() == 100


def test_add_item_invalid_price():
    cart = Cart()

    with pytest.raises(ValueError):
        cart.add_item("Mouse", -10, 1)


def test_add_item_invalid_quantity():
    cart = Cart()

    with pytest.raises(ValueError):
        cart.add_item("Mouse", 50, 0)


def test_remove_item():
    cart = Cart()
    cart.add_item("Teclado", 200, 1)

    removed = cart.remove_item("Teclado")

    assert removed is True
    assert cart.is_empty()


def test_remove_item_not_found():
    cart = Cart()
    cart.add_item("Mouse", 50, 1)

    removed = cart.remove_item("Teclado")

    assert removed is False


def test_calculate_total_multiple_items():
    cart = Cart()
    cart.add_item("Mouse", 50, 2)
    cart.add_item("Teclado", 100, 1)

    assert cart.calculate_total() == 200


def test_apply_discount():
    cart = Cart()
    cart.add_item("Monitor", 1000, 1)

    total = cart.apply_discount(0.1)

    assert total == 900


def test_invalid_discount():
    cart = Cart()
    cart.add_item("Monitor", 1000, 1)

    with pytest.raises(ValueError):
        cart.apply_discount(1.5)
