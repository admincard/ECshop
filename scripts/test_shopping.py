import unittest
from interface.interface import Interface
from common.get_result import get_result_one,get_results_all
from common.database import Database


class TestSearch_Goods(unittest.TestCase):

    def setUp(self) -> None:
        """登录"""
        # 实例化数据库
        self.DB = Database()

        self.url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/signin "
        self.method = "post"
        login_data = {
            "name": "貂蝉_10", "password": "123456"
        }
        response = Interface.login(self.method,self.url,data=login_data)
        self.session = get_result_one(response,"session")
    def test_case_01(self):
        """业务流程"""
        """点击商品"""
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/goods"
        add_data ={"goods_id":62,"session":self.session}
        response = Interface.click_goods(method=self.method,url=url,data=add_data)
        goods_id = get_result_one(response, "id")
        """加入购物车"""
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/cart/create"
        add_data = {"spec":[],"session":self.session,"goods_id":goods_id,"number":1}
        Interface.add_shopping_car(method=self.method, url=url, data=add_data)
        """进入购物车列表"""
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/cart/list"
        into_data = {"session":self.session}
        Interface.get_into_shopping(method=self.method, url=url, data=into_data)
        """选择支付方式"""
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/flow/checkOrder"
        check_data = {"session":self.session}
        response_2 = Interface.check_order(method=self.method, url=url, data=check_data)
        pay_id = get_results_all(response_2, "pay_id")[1]
        shipping_id = get_results_all(response_2, "shipping_id")[1]
        """点击提交"""
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/flow/done"
        click_data ={"shipping_id":shipping_id,
                     "session":self.session,"pay_id":pay_id}
        response_3 = Interface.check_order(method=self.method, url=url, data=click_data)
        order_id = get_result_one(response_3,"order_id")
        """下单支付"""
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/order/pay"
        pay_data = {"session":self.session,"order_id":order_id}
        pay_response = Interface.order_pay(method=self.method,url=url,data=pay_data)
        res = get_result_one(pay_response,"succeed")
        self.assertEqual(res,1,msg="购买商品失败")
    def test_case_02(self):
        """购物车的增删改查"""
        """点击商品"""
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/goods"
        add_data = {"goods_id": 37, "session": self.session}
        response = Interface.click_goods(method=self.method, url=url, data=add_data)
        goods_id = get_result_one(response, "id")
        """加入购物车"""
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/cart/create"
        add_data = {"spec": [], "session": self.session, "goods_id": goods_id, "number": 1}
        Interface.add_shopping_car(method=self.method, url=url, data=add_data)
        """更新购物车"""
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/cart/update"
        update_data = {"new_number":"1","session":self.session,"rec_id":8933}
        Interface.update_shopping(method=self.method,url=url,data=update_data)   # 获取返回值
        """移除购物车"""
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/cart/delete"
        remove_data = {"session":self.session,"rec_id":8994}
        remove_response = Interface.remove_shopping(method=self.method,url=url,data=remove_data)
        """查看数据库"""
        goods_amount = get_result_one(remove_response, "goods_amount")
        sql = f'select count(*) from ecs_order_info where order_sn = "{goods_amount}"'
        datas = self.DB.one(sql)
        data = datas['count(*)']
        self.assertEqual(data,0,"购物车增删改查失败")  # 断言商品数量等于0
if __name__ == '__main__':
    unittest.main()

