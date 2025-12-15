from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_complete_purchase_flow(driver):
    login = LoginPage(driver)
    login.load()
    login.login("standard_user", "secret_sauce")

    inventory = InventoryPage(driver)
    inventory.add_product_to_cart()
    inventory.go_to_cart()

    assert "cart" in driver.current_url
