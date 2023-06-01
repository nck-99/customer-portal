import time

from pageObject.DashBoard import OrdersTab

class TestScheduleDelivery:

    def test_schedule_delivery(self, setup):
        ot = OrdersTab(setup)
        ot.click_dashboard(setup)
        ot.create_schedule_delivery()
        ot.add_order_details()
        time.sleep(3)
        ot.save_schedule_order()

    def test_select_delete_order(self, setup):
        ot = OrdersTab(setup)
        ot.click_dashboard(setup)
        ot.select_order()
        time.sleep(3)
        ot.delete_line_item()
        time.sleep(3)
        assert ot.verify() == True




