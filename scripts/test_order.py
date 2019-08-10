import unittest
from interface.interface import Interface
from common.get_result import get_result_one
from scripts.test_login import Login
from common.database import Database

class WaitOrder(unittest.TestCase):
    def setUp(self):
        self.session = Login.login()
        self.db = Database()

    def order(self):
        """查看待付款订单"""
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/order/list"
        method = "post"
        data = {"session":self.session,
                "type":"await_pay",
                "pagination":{"count":10,"page":1}}
        response = Interface.wait_pay_list(method=method,url=url,data=data)
        order_id = get_result_one(response,"order_id")
        order_sn = get_result_one(response,'order_sn')
        status = get_result_one(response, "succeed")
        self.assertEqual(status, 1)
        return order_id,order_sn
    def test_01(self):
        """查看待付款订单"""
        order_id = self.order()[0]
        order_sn = self.order()[1]

        sql = "SELECT *from ecs_order_info where user_id = '4349' and order_id = '2659'"
        data = self.db.one(sql)
        info = data['order_sn']
        self.assertEqual(info,order_sn,msg="代付款订单信息错误")
    def test_02(self):
        """取消订单"""
        order_id = self.order()
        del_url = "http://ecshop.itsoso.cn/ECMobile/?url=/order/cancel"
        method = "post"
        del_data = {"session":self.session,
                "order_id":f"{order_id}"}
        response = Interface.del_order(method=method,url=del_url,data=del_data)
        status = get_result_one(response, "succeed")
        # print(SendMethod.response_dumps(response))
        self.assertEqual(status, 1,msg="代付款取消订单失败")

    def test_03(self):
        """点击付款"""
        order_id = self.order()
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/order/pay"
        method = "post"
        data = {"session":self.session,
                "order_id":order_id}
        response = Interface.pay(method=method, url=url, data=data)
        status = get_result_one(response, "succeed")
        self.assertEqual(status, 1,msg="付款失败")
    def test05(self):
        """点击确认收货"""
        order_id = self.order()
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/order/affirmReceived"
        method = "post"
        data = {"session":self.session,
                "order_id":order_id}
        response = Interface.sure_shouhuo(method=method,url=url,data=data)
        status = get_result_one(response, "succeed")
        self.assertEqual(status, 1,msg="待收货确认收货失败")


if __name__ == '__main__':
    unittest.main()