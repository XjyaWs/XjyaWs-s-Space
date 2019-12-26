"""
基于pymysql模块，MySQL数据库实现简易版本的用户登录注册
"""
import pymysql


class Db_handler(object):
    def __init__(self):
        # 与数据库建立连接
        conn = pymysql.connect(
            user='root',
            passwd='xjyaws',
            host='127.0.0.1',
            port=3306,
            database='day41',
            charset='utf8',
            autocommit=True    # 对数据库产生的变动自动提交
        )

        self.cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    def save(self, usr, pwd):
        """
        对用户数据进行存储
        :param usr: 用户名
        :param pwd: 用户密码
        :return:
        """
        # 开启事务
        self.cursor.execute('start transaction')

        # 进行数据录入
        try:
            sql1 = 'insert into ex2(usr, pwd) values ("{}", "{}")'.format(usr, pwd)
            self.cursor.execute(sql1)
        except Exception:
            self.cursor.execute('rollback')    # 若出错 事务回档
            print('注册失败')
        else:
            self.cursor.execute('commit')    # 若无错 事务提交
            print('注册成功')

    def check_user(self, usr):
        """
        检测用户名是否存在
        :param usr: 用户名
        :return: True 存在，False 不存在
        """
        sql1 = 'select * from ex2 where usr = "{}"'.format(usr)
        res = self.cursor.execute(sql1)
        if res:
            return True
        else:
            return False

    def check_login(self, usr, pwd):
        """
        登录检测
        :param usr: 用户名
        :param pwd: 用户密码
        :return: True：用户名密码正确 False：用户名密码不正确
        """
        # 为了防止sql注入，这里使用cursor.execute进行sql语句的拼接，拼接方式如下
        sql1 = "select * from ex2 where usr = %s and pwd = %s"
        res = self.cursor.execute(sql1, (usr, pwd))
        if res:
            return True
        else:
            return False


class Interface(object):
    user_interface = "请选择功能：\n1. 注册\n2. 登录\n\n输入代表功能的数字>>>:"
    db_handler = Db_handler()    # 数据库接口对象的建立

    def __init__(self):
        # 初始化界面
        choice1 = input(self.user_interface).strip()

        # 选择功能 1注册 2登录
        if choice1 == '1':
            self.register()
        elif choice1 == '2':
            self.login()

        # 询问是否继续还是退出
        choice2 = input('是否继续操作？输入Q以退出\n请输入>>>:').strip()
        if choice2 != 'Q':
            self.__init__()    # 不退出时进行回环

    def register(self):
        # 用户创建用户名
        while True:
            usr = input('请输入用户名>>>：').strip()

            # 检测用户名是否存在
            if not self.db_handler.check_user(usr):
                break

            print('用户名已存在')

        # 用户输入密码
        while True:
            pwd = input('请输入密码>>>：').strip()
            pwd_check = input('请确认密码>>>：').strip()
            if pwd == pwd_check:
                break
            print('密码不一致')

        # 储存用户密码到数据库
        self.db_handler.save(usr, pwd)

    def login(self):
        # 用户登录，输入用户名密码
        usr = input('请输入用户名>>>：').strip()
        pwd = input('请输入密码>>>：').strip()

        # 检测登录
        if self.db_handler.check_login(usr, pwd):
            print('登录成功')
        else:
            print('用户名或密码不存在')


if __name__ == '__main__':
    interface = Interface()
