from selenium import webdriver
import pytest


@pytest.fixture()
def setup():
    browser = webdriver.Chrome()
    browser.get("https://ibpodev.home.tatamotors/edukaan_ui/#/")
    browser.maximize_window()
    browser.implicitly_wait(10)
    yield browser
    browser.quit()