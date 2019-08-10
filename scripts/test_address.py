import unittest
from common.get_result import get_result_one
from interface.interface import Interface
from scripts.test_login import Login
from common.database import Database
import ddt,os
from common.operationexcel import OperationExcel
ADDRESS_FILE = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0]
config = os.path.join(ADDRESS_FILE,'data','address_data.xlsx')
opear = OperationExcel(config)
test_data = opear.get_data_for_dict()
@ddt.ddt
class TestAddress(unittest.TestCase):
    def setUp(self):
        self.session = Login.login()
        self.db = Database()
    def test_address_01(self):
        """新增地址--合法数据"""
        #测试之前先查看数量
        sql = "select count(*) from ecs_user_address where user_id = (select user_id from ecs_users where user_name = 'hxj123456')"
        datas = self.db.one(sql)
        num = datas['count(*)']
        add_url = "http://ecshop.itsoso.cn/ECMobile/?url=/address/add"#新增地址的网址
        method = "post"
        add_data = {"address":{"default_address":0,
                               "consignee":"han123",
                               "tel":"13350438199",
                               "zipcode":"620042",
                               "country":"1",
                               "city":"37",
                               "id":0,
                               "email":"156435343@qq.com",
                               "address":"121321",
                               "province":"2",
                               "district":"404",
                               "mobile":""},
                    "session":self.session}
        Interface.add_dress(method=method,url=add_url,data=add_data)#请求新增地址的接口
        """新增之后查看数量"""
        datas_2 = self.db.one(sql)
        new_num = datas_2['count(*)']
        self.assertEqual(new_num, num +1)

    @ddt.data(*test_data)
    def test_address_02(self, data):
        """新增收货地址---非法数据"""
        sql = "select count(*) from ecs_user_address where user_id = (select user_id from ecs_users where user_name = 'hxj123456')"
        datas = self.db.one(sql)
        old = datas['count(*)']
        add_url = "http://ecshop.itsoso.cn/ECMobile/?url=/address/add"  # 新增地址的网址
        method = "post"
        add_data = {"address": {"default_address": 0,
                                "consignee": f"{data['consignee']}",
                                "tel": f"{data['tel']}",
                                "zipcode": "",
                                "country": "1",
                                "city": "151",
                                "id": 0,
                                "email": f"{data['email']}",
                                "address": f"{data['address']}",
                                "province": "14",
                                "district": "1603",
                                "mobile": ""},
                    "session": self.session}
        Interface.upd_dress(method=method, url=add_url, data=add_data)
        data = self.db.one(sql)
        news = data['count(*)']
        self.assertEqual(old, news,msg="新增地址用非法数据新增成功")
    def address_03(self):
        """查看收货地址"""
        look_url = "http://ecshop.itsoso.cn/ECMobile/?url=/address/list"#查看收货地址的网址
        method = 'post'
        look_data = {"session":self.session}
        lool_response = Interface.look_dress(method=method, url=look_url, data=look_data)#请求查看地址的接口
        id  = get_result_one(lool_response,"id")
        return id

    def test_address_03(self):
        """查看收货地址"""
        self.address_03()
    def test_address_04(self):
        """修改收货地址"""
        id = self.address_03()
        print(id)
        upd_url = "http://ecshop.itsoso.cn/ECMobile/?url=/address/update"#修改收货地址的网址
        method = "post"
        consignee = '韩小居'
        upd_data = {"address":{"default_address":0,
                               "consignee":f"{consignee}",
                               "tel":"12315456",
                               "zipcode":"",
                               "country":"1",
                               "city":"151",
                               "id":0,
                               "email":"12346464@qq.com",
                               "address":"天府新谷1",
                               "province":"14",
                               "district":"1603",
                               "mobile":""},
                    "address_id":f"{id}",
                    "session":self.session}
        Interface.upd_dress(method=method,url=upd_url,data=upd_data)
        sql  =f'select consignee from ecs_user_address where address_id = "{id}"'
        data = self.db.one(sql)
        name = data['consignee']
        self.assertEqual(consignee,name)
    @ddt.data(*test_data)
    def test_address_05(self,data):
        """修改收货地址---非法数据"""
        id = self.address_03()
        sql = f'select consignee from ecs_user_address where address_id = "{id}"'
        old = self.db.one(sql)
        olds = old['consignee']
        upd_url = "http://ecshop.itsoso.cn/ECMobile/?url=/address/update"#修改收货地址的网址
        method = "post"
        upd_data = {"address":{"default_address":0,
                               "consignee":f"{data['consignee']}",
                               "tel":f"{data['tel']}",
                               "zipcode":"",
                               "country":"1",
                               "city":"151",
                               "id":0,
                               "email":f"{data['email']}",
                               "address":f"{data['address']}",
                               "province":"14",
                               "district":"1603",
                               "mobile":""},
                    "address_id":f"{id}",
                    "session":self.session}
        Interface.upd_dress(method=method,url=upd_url,data=upd_data)
        data = self.db.one(sql)
        news = data['consignee']
        self.assertEqual(olds,news,msg="修改收货地址--使用非法数据修改成功")
    def test_address_06(self):
        """删除收货地址"""
        #删除之前查看数量
        id = self.address_03()
        sql = "select count(*) from ecs_user_address where user_id = (select user_id from ecs_users where user_name = 'hxj123456')"
        datas = self.db.one(sql)
        num = datas['count(*)']
        del_url = "http://ecshop.itsoso.cn/ECMobile/?url=/address/delete"#删除地址的网址
        method = "post"
        del_data = {"address_id":f"{id}",
                    "session":self.session}
        Interface.del_dress(method=method,url=del_url,data=del_data)
        #删除之后查看数量
        datas_2 = self.db.one(sql)
        new_num = datas_2['count(*)']
        #断言,查看删除前和删除后是否一致
        self.assertEqual(new_num,num-1,msg="删除数据失败")

if __name__ == '__main__':
    unittest.main()
