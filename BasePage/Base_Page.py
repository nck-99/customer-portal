import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

@pytest.mark.usefixtures()
class BasePage():
    def __init__(self, setup):
        self.driver = setup

    def find_element(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def find_all_elements(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator))

    def find (self, locator):
        return self.driver.find_element(locator)

    def locate_by_invisibility(self, locator):
        return EC.invisibility_of_element_located(locator)

    def locate_by_visibility(self, locator):
        return EC.visibility_of_any_elements_located(locator)

    def wait (self, time):
        return self.driver.implicitly_wait(time)

    def current_url(self):
        return self.driver.current_url

    def actionScroll(self, locator):
        actions = ActionChains(self.driver)
        return actions.scroll_to_element(locator)

