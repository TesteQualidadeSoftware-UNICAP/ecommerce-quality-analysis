import pytest
from src.cart import Cart
from src.order import Order


def create_cart():
    cart = Cart()
    cart.add_item("Mouse", 100, 1)
    return cart


def test_create_order_success():
    cart = create_cart()

    order = Order(cart, "Ana", "Recife")

    assert order.customer_name == "Ana"
    assert order.status == "created"
    assert order.total == 100


def test_create_order_with_empty_cart():
    cart = Cart()

    with pytest.raises(ValueError):
        Order(cart, "Ana", "Recife")


def test_calculate_shipping_local():
    cart = create_cart()
    order = Order(cart, "João", "Recife")

    shipping = order.calculate_shipping("PE")

    assert shipping == 20


def test_calculate_shipping_other_state():
    cart = create_cart()
    order = Order(cart, "Carlos", "Recife")

    shipping = order.calculate_shipping("SP")

    assert shipping == 50


def test_apply_coupon_valid():
    cart = create_cart()
    order = Order(cart, "Maria", "Recife")

    order.apply_coupon("PROMO10")

    assert order.total == 90


def test_apply_coupon_invalid():
    cart = create_cart()
    order = Order(cart, "Maria", "Recife")

    with pytest.raises(ValueError):
        order.apply_coupon("INVALIDO")


def test_finalize_order_paid():
    cart = create_cart()
    order = Order(cart, "Pedro", "Recife")

    order.finalize_order(True)

    assert order.status == "paid"


def test_finalize_order_pending():
    cart = create_cart()
    order = Order(cart, "Pedro", "Recife")

    order.finalize_order(False)

    assert order.status == "pending"


def test_cancel_order():
    cart = create_cart()
    order = Order(cart, "Pedro", "Recife")

    order.cancel_order()

    assert order.status == "cancelled"


def test_cancel_paid_order():
    cart = create_cart()
    order = Order(cart, "Pedro", "Recife")

    order.finalize_order(True)

    with pytest.raises(Exception):
        order.cancel_order()
