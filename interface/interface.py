"""
添加被测试的接口
"""
from common.sendmethod import SendMethod


class Interface:
    @ staticmethod
    def register(method,url,data):
        """注册接口"""
        return SendMethod.send_method(method=method, url=url, data=data)
    @staticmethod
    def login(method,url,data):
        """登录接口"""
        return SendMethod.send_method(method=method, url=url, data=data)
    @staticmethod
    def add_dress(method,url,data):
        """新增收货地址"""
        return SendMethod.send_method(method=method, url=url, data=data)
    @staticmethod
    def upd_dress(method,url,data):
        """修改地址"""
        return SendMethod.send_method(method=method, url=url, data=data)
    @staticmethod
    def del_dress(method,url,data):
        """删除地址"""
        return SendMethod.send_method(method=method, url=url,data=data)
    @staticmethod
    def look_dress(method,url,data):
        """查看收货地址"""
        return SendMethod.send_method(method=method,url=url,data=data)
    @staticmethod
    def add_collection(method,url,data):
        """添加收藏商品"""
        return SendMethod.send_method(method=method, url=url,data=data)
    @staticmethod
    def del_collection(method, url,data):
        """删除收藏的商品"""
        return SendMethod.send_method(method=method, url=url,data=data)
    @staticmethod
    def look_collection(method, url,data):
        """查看收藏的商品"""
        return SendMethod.send_method(method=method, url=url,data=data)

    @staticmethod
    def search_shop(method, url, data):
        """搜索商品"""
        return SendMethod.send_method(method=method, url=url, data=data)

    @staticmethod
    def click_shop(method, url, data):
        """点击商品"""
        return SendMethod.send_method(method=method, url=url, data=data)

    @staticmethod
    def add_car(method, url, data):
        """加入购物车"""
        return SendMethod.send_method(method=method, url=url, data=data)

    @staticmethod
    def car_list(method, url, data):
        """购物车列表"""
        return SendMethod.send_method(method=method, url=url, data=data)

    @staticmethod
    def upd_car(method, url, data):
        """更新购物车"""
        return SendMethod.send_method(method=method, url=url, data=data)

    @staticmethod
    def remove_car(method, url, data):
        """删除购物车"""
        return SendMethod.send_method(method=method, url=url, data=data)

    @staticmethod
    def check_order(method, url, data):
        """选择支付方式"""
        return SendMethod.send_method(method=method, url=url, data=data)

    @staticmethod
    def click_submit(method, url, data):
        """点击提交"""
        return SendMethod.send_method(method=method, url=url, data=data)

    @staticmethod
    def wait_pay_list(method, url, data):
        """查看待付款订单"""
        return SendMethod.send_method(method=method, url=url, data=data)

    @staticmethod
    def pay(method, url, data):
        """付款"""
        return SendMethod.send_method(method=method, url=url, data=data)

    @staticmethod
    def del_order(method, url, data):
        """取消订单"""
        return SendMethod.send_method(method=method, url=url, data=data)

    @staticmethod
    def send_good(method, url, data):
        """查看待发货"""
        return SendMethod.send_method(method=method, url=url, data=data)

    @staticmethod
    def sure_shouhuo(method, url, data):
        """确认收货"""
        return SendMethod.send_method(method=method, url=url, data=data)


    @staticmethod
    def test_obligation(method, url, data):
        """测试待付款"""
        return SendMethod.send_method(method=method, url=url, data=data)

    @staticmethod
    def test_deoder(method, url, data):
        """取消订单"""
        return SendMethod.send_method(method=method, url=url, data=data)

    @staticmethod
    def test_payment(method, url, data):
        """付款"""
        return SendMethod.send_method(method=method, url=url, data=data)

    @staticmethod
    def test_beshipped(method, url, data):
        """待发货"""
        return SendMethod.send_method(method=method, url=url, data=data)

    @staticmethod
    def test_bereceived(method, url, data):
        """待收货"""
        return SendMethod.send_method(method=method, url=url, data=data)

    @staticmethod
    def test_collection(method, url, data):
        """查看收藏"""
        return SendMethod.send_method(method=method, url=url, data=data)

    @staticmethod
    def test_addcollection(method, url, data):
        """添加收藏"""
        return SendMethod.send_method(method=method, url=url, data=data)

    @staticmethod
    def test_delcollection(method, url, data):
        """删除收藏"""
        return SendMethod.send_method(method=method, url=url, data=data)

    @staticmethod
    def test_address(method, url, data):
        """查看收货地址"""
        return SendMethod.send_method(method=method, url=url, data=data)

    @staticmethod
    def test_addaddress(method, url, data):
        """添加收货地址"""
        return SendMethod.send_method(method=method, url=url, data=data)

    @staticmethod
    def test_deladdress(method, url, data):
        """删除收货地址"""
        return SendMethod.send_method(method=method, url=url, data=data)

    @staticmethod
    def test_postaddress(method, url, data):
        """修改收货地址"""
        return SendMethod.send_method(method=method, url=url, data=data)

    @staticmethod
    def test_setdefault(method, url, data):
        """设置默认收货地址"""
        return SendMethod.send_method(method=method, url=url, data=data)

    @staticmethod
    def search_goods(method,url,data):
        """搜索商品"""
        return SendMethod.send_method(method=method,url=url,data=data)
    @staticmethod
    def click_goods(method,url,data):
        """点击商品"""
        return SendMethod.send_method(method=method,url=url,data=data)
    @staticmethod
    def add_shopping_car(method,url,data):
        """加入购物车"""
        return SendMethod.send_method(method=method,url=url,data=data)

    @staticmethod
    def get_into_shopping(method,url,data):
        """进入购物车"""
        return SendMethod.send_method(method=method,url=url,data=data)
    @staticmethod
    def update_shopping(method,url,data):
        """更新购物车"""
        return SendMethod.send_method(method=method,url=url,data=data)

    @staticmethod
    def remove_shopping(method,url,data):
        """移除购物车"""
        return SendMethod.send_method(method=method,url=url,data=data)

    @staticmethod
    def order_pay(method,url,data):
        """下单支付"""
        return SendMethod.send_method(method=method,url=url,data=data)

