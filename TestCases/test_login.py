from pageObject.AdminLoginPage import Login

class testLogin:
    baseUrl = "https://ibpodev.home.tatamotors/edukaan_Admin/#/session/Login"
    username = "SSV533008"
    password = "Tml@0323"

    def test_page_title(self, setup):
        self.driver=setup
        self.driver.get(self.baseUrl)
        title=self.driver.title
        if title=="e-Dukaan | Login":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots" + "test_login.png")
            self.driver.close()
            assert False

    def test_login(self, setup):
        self.driver=setup
        self.driver.get(self.baseUrl)
        self.lp=Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        title=self.driver.title
        if title=="e-Dukaan | Dashboard":
            assert True
            self.driver.close()
        else:
            self.driver.save_screenshot(".\\Screenshots" + "test_login.png")
            self.driver.close()
            assert False



