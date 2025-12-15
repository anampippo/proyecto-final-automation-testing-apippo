import json
import pytest
import os
from pages.login_page import LoginPage
from utils.driver_factory import get_driver
from utils.screenshot import take_screenshot

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def load_users():
    base_dir = os.path.dirname(__file__)
    file_path = os.path.join(base_dir, "users.json")

    with open(file_path, "r", encoding="utf-8") as f:
        return json.load(f)

def test_login_success(driver):
    users = load_users()
    login = LoginPage(driver)
    login.load()
    login.login(users["valid_user"]["username"], users["valid_user"]["password"])
    assert "inventory" in driver.current_url

def test_login_invalid(driver):
    users = load_users()
    login = LoginPage(driver)
    login.load()
    login.login(users["invalid_user"]["username"], users["invalid_user"]["password"])
    screenshot = take_screenshot(driver, "test_login_invalid")
    assert "Epic sadface" in login.get_error()
