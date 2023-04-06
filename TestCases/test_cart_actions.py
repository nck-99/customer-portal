import time
from pageObject import SETPassword
from pageObject import WhishList
from pageObject import CartActions

class Test_CartActions:

    def test_add_to_cart(self, setup):
        sp = SETPassword.SetPassword(setup)
        sp.static_login(setup)
        wl = WhishList.Whish_List(setup)
        wl.search_part("Wheel")
        time.sleep(5)
        wl.select_part()
        ca = CartActions.Cart_Actions(setup)
        ca.add_to_cart()
        time.sleep(9)
        ca.view_cart()
        assert ca.Verify_cart_item() == True

    def test_neg_add_to_cart(self, setup):
        sp = SETPassword.SetPassword(setup)
        sp.static_login(setup)
        wl = WhishList.Whish_List(setup)
        wl.search_part("Wheel")
        time.sleep(5)
        wl.select_part()
        ca = CartActions.Cart_Actions(setup)
        ca.add_to_cart()
        print(wl.container_msg())
        assert wl.container_msg() == "Product already exist."

    def test_remove_from_cart(self, setup):
        sp = SETPassword.SetPassword(setup)
        sp.static_login(setup)
        ca = CartActions.Cart_Actions(setup)
        ca.view_cart()
        ca.clear_cart()
        wl = WhishList.Whish_List(setup)
        assert wl.container_msg() == "Cleared all cart successfully"

