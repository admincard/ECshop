#导入pymysql
import pymysql

class Database(object):
    def __init__(self,host="ecshop.itsoso.cn",user='ecshop',
                 password = "ecshop",database = "ecshop",charset="utf8"):
        #绑定属性
        #创建连接
        self.con = pymysql.connect(host = host,
                                   user= user,
                                   password = password,
                                   database = database,
                                   charset =charset)

        self.cursor = self.con.cursor(cursor=pymysql.cursors.SSDictCursor)

    def execute(self,sql,args=None):
        #执行写操作
        try:
            # 开启事务
            self.con.begin()
            #执行sql
            num = self.cursor.execute(sql,args)
            if num > 0:
                # 提交事务
                self.con.commit()
                return True
            else:
                # 回滚事务
                self.con.rollback()
                return False
        except Exception as e:
            # 回滚
            self.con.rollback()
            return False

    def __del__(self):
        #关闭游标和连接
        self.cursor.close()
        self.con.close()

    def all(self,sql,args=None):
        #读取所有数据
        #执行sql
        self.cursor.execute(sql,args)
        #通过游标获取所有数据
        return self.cursor.fetchall()

    def one(self,sql,args=None):
        # 读取一行数据
        # 执行sql
        self.cursor.execute(sql, args)
        # 通过游标获取一行数据
        return self.cursor.fetchone()


if __name__ == '__main__':
    db = Database()  # 创建对象
    # from database import Database
    # db = Database(password="root", database="class")
    # sql = 'select count(*) from ecs_order_info where order_sn = "2019072484960"'
    # datas = db.one(sql)
    # print(datas)
    # sql = "select count(*) from ecs_user_address where user_id = (select user_id from ecs_users where user_name = 'hxj123456')"
    # datas = db.one(sql)
    # data = datas['count(*)']
    # print(data)

    sql = "SELECT *from ecs_order_info where user_id = '4349' and order_id = '2231'"
    data = db.one(sql)
    print(data)