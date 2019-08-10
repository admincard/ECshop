import unittest
from interface.interface import Interface
from common.get_result import get_result_one
from scripts.test_login import Login
from common.database import Database



class TestCollect(unittest.TestCase):
    def setUp(self):
        self.sid,self.uid = Login.login()
        self.db = Database()

    def test_collect_01(self):
        """收藏商品"""
        url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/collect/create"  # 添加收藏的网址
        method = "post"
        add_collect_data = {"session":{"uid":f"{self.uid}","sid":f"{self.sid}"},"goods_id":64}
        Interface.add_collection(method=method,url=url,data=add_collect_data)#请求添加收藏接口
        sql = 'select count(*) from ecs_collect_goods where user_id="4349" and goods_id="64"'
        data = self.db.one(sql)
        num = data['count(*)']
        self.assertEqual(num,1)
    def test_collect_02(self):
        """查看收藏的商品"""
        res = self.check_goods()[1]
        sql = 'select count(*) from ecs_collect_goods where user_id="4349"'
        data = self.db.one(sql)
        nums = data['count(*)']
        self.assertEqual(int(res),nums)
    def check_goods(self):
        """查看收藏的商品"""
        look_url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/collect/list"#查看收藏的网址
        method = 'post'
        look_data ={"session":{"uid":f"{self.uid}","sid":f"{self.sid}"},
                    "pagination":{"count":10,"page":1},
                    "rec_id":0}
        look_response = Interface.look_collection(method=method,url=look_url,data=look_data)#请求查看收藏的接口
        total = get_result_one(look_response,'total')
        rec_id = get_result_one(look_response,"rec_id")
        print(rec_id)
        return rec_id,total

    def test_collect_03(self):
        """删除收藏的商品"""
        rec_id = self.check_goods()[0]
        del_url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/collect/delete"#删除收藏的网址
        method = "post"
        del_data = {"session":{"uid":f"{self.uid}","sid":f"{self.sid}"},
                    "rec_id":f"{rec_id}"}
        Interface.del_collection(method=method, url=del_url,data=del_data)

        sql = f'select count(*) from ecs_collect_goods where user_id="4349" and rec_id="{rec_id}"'
        datas = self.db.one(sql)
        data = datas["count(*)"]
        self.assertEqual(data,0)
		


if __name__ == '__main__':
    unittest.main()


