from common.operationexcel import OperationExcel
import unittest
from common.database import Database
from common.get_result import get_result_one
import ddt,os
from faker import Faker

from interface.interface import Interface

BASE_PATH = os.path.split(os.path.dirname(os.path.realpath(__file__)))[0] # 获取当前目录--获取项目目录
ERROR_FILE = os.path.join(BASE_PATH,'data','test_data.xlsx')  # 将"data"文件夹添加到当前目录
error_oper = OperationExcel(ERROR_FILE)
test_datas= error_oper.get_data_for_dict()


@ddt.ddt
class Test_Register(unittest.TestCase):

    def setUp(self):
        self.url = "http://ecshop.itsoso.cn/ECMobile/?url=/user/signup"  # 请求地址
        self.method = 'post'  # 请求方式
        # 实例化DB
        self.db = Database()
        self.fk = Faker('zh_CN')

    def test_case_01(self):
        """正向数据注册成功"""
        name = self.fk.user_name() # 姓名
        email = self.fk.email()  # 邮箱
        phone = self.fk.phone_number()  # 手机号
        password = self.fk.password() # 密码
        id = self.fk.pyint()  # 随机整数
        data = {"field": [{"id": id, "value": f"{phone}"}],
                "email": f"{email}", "name": f"{name}",
                "password": f"{password}"}
        response = Interface.register(method='post',url=self.url,data=data)

        #查看数据库是否注册成功
        sql = f"select count(*) from ecs_users where user_name = '{name}'"
        datas = self.db.one(sql)
        num = datas['count(*)']
        self.assertEqual(num,1,msg="合法数据注册失败")

        #将测试数据删除
        del_sql = f"delete from ecs_users where user_name='{name}'"
        self.db.execute(del_sql)

    @ddt.data(*test_datas)
    def test_case_02(self, data):
        req_data = {"field": [{"id": 5, "value": data["phone"]}],
                    "email": data["email"],
                    "name": data["name"],
                    "password": data["password"]}

        response = Interface.register(method="post", url=self.url, data=req_data)
        status = get_result_one(response, "succeed")
        self.assertEqual(status,0)

        # 查找数据库
        sql = f"select count(*) from ecs_users where user_name = '{data['name']}';"
        datas = self.db.one(sql)
        data = datas['count(*)']  # data==0
        self.assertEqual(data, 0,msg="逆向数据注册成功")
if __name__ == '__main__':
    unittest.main()
