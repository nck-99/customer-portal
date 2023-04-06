import time
from pageObject import SETPassword
from pageObject import WhishList

class Test_WhishList:
    def test_add_whishlist(self, setup):
        sp = SETPassword.SetPassword(setup)
        sp.static_login(setup)
        wl = WhishList.Whish_List(setup)
        wl.search_part("Wheel")
        time.sleep(5)
        wl.select_part()
        wl.wait(7)
        wl.add_whishlist()
        time.sleep(7)
        wl.view_whishlist()
        time.sleep(7)
        assert wl.verify_whishlist_item() == True

    def test_empty_whishlist(self, setup):
        sp = SETPassword.SetPassword(setup)
        sp.static_login(setup)
        wl = WhishList.Whish_List(setup)
        time.sleep(5)
        wl.view_whishlist()
        wl.empty_whishlist()
        assert wl.check_msg() == 1

    def test_remove_from_whishlist(self, setup):
        sp = SETPassword.SetPassword(setup)
        sp.static_login(setup)
        wl = WhishList.Whish_List(setup)
        wl.search_part("Wheel")
        time.sleep(5)
        wl.select_part()
        wl.wait(7)
        wl.add_whishlist()
        time.sleep(7)
        wl.view_whishlist()
        wl.select_all()
        wl.remove()
        assert wl.check_msg() == 1

    def test_move_to_cart(self, setup):
        sp = SETPassword.SetPassword(setup)
        sp.static_login(setup)
        wl = WhishList.Whish_List(setup)
        wl.search_part("Wheel")
        time.sleep(5)
        wl.select_part()
        wl.wait(7)
        wl.add_whishlist()
        time.sleep(7)
        wl.view_whishlist()
        wl.select_all()
        wl.move_to_cart()
        assert wl.check_msg() == 1

    def test_neg_add_to_whishlist(self, setup):
        sp = SETPassword.SetPassword(setup)
        sp.static_login(setup)
        wl = WhishList.Whish_List(setup)
        wl.search_part("Wheel")
        time.sleep(5)
        wl.select_part()
        wl.wait(7)
        wl.add_whishlist()
        time.sleep(7)
        wl.view_whishlist()
        time.sleep(7)
        assert wl.verify_whishlist_item() == True
        wl.search_part("Wheel")
        time.sleep(5)
        wl.select_part()
        wl.wait(7)
        wl.add_whishlist()
        if wl.check_msg() == 0:
            assert True
