"""
3.定义一个时间 Timedate 类
    一个初始化方法，可以初始化对象属性datetime，属性类型就是datetime类型，如果外界传了就是外界传入的时间，如果没有传入默认就采用当前系统时间
    一个绑定给对象的方法get_season，可以得到当前对象所在时间对应的季节(1~3月代表春季)
    一个静态类(普通函数)方法get_now_season，获取当前系统时间所存的季节
    一个绑定给类的方法get_next_season，利用get_now_season方法得到即将到来的季节
"""
import datetime


class Timedate(object):
    def __init__(self, *args: datetime.datetime):
        if args != ():
            self.datetime = args[0]
        else:
            self.datetime = datetime.datetime.today()

    def get_season(self):
        if 1 <= self.datetime.month <= 3:
            return 'Spring'
        elif 4 <= self.datetime.month <= 6:
            return 'Summer'
        elif 7 <= self.datetime.month <= 9:
            return 'Autumn'
        elif 10 <= self.datetime.month <= 12:
            return 'Winter'

    @staticmethod
    def get_now_season():
        if 1 <= datetime.datetime.today().month <= 3:
            return 'Spring'
        elif 4 <= datetime.datetime.today().month <= 6:
            return 'Summer'
        elif 7 <= datetime.datetime.today().month <= 9:
            return 'Autumn'
        elif 10 <= datetime.datetime.today().month <= 12:
            return 'Winter'

    @classmethod
    def get_next_season(cls):
        list1 = ['Spring', 'Summer', 'Autumn', 'Winter']
        for index, season in enumerate(list1):
            if season == cls.get_now_season():
                return list1[(index + 1) % len(list1)]


if __name__ == '__main__':
    time1 = Timedate(datetime.datetime(2017, 1, 1))
    print(time1.get_next_season())

# Spring
