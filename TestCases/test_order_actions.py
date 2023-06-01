import time
from pageObject import OrdersPage

class TestCartActions:
    def test_add_to_cart(self, setup):
        op = OrdersPage.Orders(setup)
        op.add_to_cart(setup, "Wheel")
        assert op.verify_add_cart(setup) == True

    def test_remove_from_cart(self, setup):
        op = OrdersPage.Orders(setup)
        op.remove_from_cart(setup)
        time.sleep(2)
        assert op.verify_remove_cart() == True

    def test_empty_cart(self, setup):
        op = OrdersPage.Orders(setup)
        op.add_to_cart(setup, "Wheel")
        time.sleep(5)
        assert op.empty_cart(setup) == True

class Test_PlaceOrder_CancelOrder():

    def test_place_order(self, setup):
        op = OrdersPage.Orders(setup)
        op.add_to_cart(setup, "Wheel")
        if op.verify_add_cart(setup) == True:
            time.sleep(5)
            op.place_order(setup)
            op.move_to_payment()
            assert bool(op.verify_order_no()) == 1

    def test_cancel_order(self, setup):
        op = OrdersPage.Orders(setup)
        op.cancel_order(setup)
        time.sleep(5)
        assert op.verify_cancel_order(setup) == True

