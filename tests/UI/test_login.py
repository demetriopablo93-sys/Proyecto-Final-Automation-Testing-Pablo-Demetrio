import pytest
from pages.login_page import LoginPage


@pytest.mark.ui
class TestLogin:
    def test_login_success(self, driver_scope):
        page = LoginPage(driver_scope)
        page.go()
        page.login('standard_user', 'secret_sauce')
        from pages.inventory_page import InventoryPage
        inv = InventoryPage(driver_scope)
        assert 'Products' in inv.title_text()


    def test_login_fail(self, driver_scope):
        page = LoginPage(driver_scope)
        page.go()
        page.login('locked_out_user', 'wrong_password')
        assert 'Epic sadface' in page.get_error()