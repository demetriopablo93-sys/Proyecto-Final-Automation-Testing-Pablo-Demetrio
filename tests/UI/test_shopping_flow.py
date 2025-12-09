import pytest
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage


@pytest.mark.ui
def test_add_to_cart_and_count(driver_scope):
    login = LoginPage(driver_scope)
    login.go()
    login.login('standard_user', 'secret_sauce')

    inv = InventoryPage(driver_scope)

    # Agregar producto
    inv.add_first_item()

    # Ir al carrito
    inv.go_to_cart()

    # Validar carrito
    cart = CartPage(driver_scope)
    count = cart.count_items()

    print("DEBUG - items in cart:", count)

    assert count >= 1, f"Expected at least 1 item in cart, got {count}"
