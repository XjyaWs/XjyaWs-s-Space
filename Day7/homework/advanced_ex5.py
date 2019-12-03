"""
5.定义一个国家类 Country 类，可以初始化name，area（所在的大州）两个属性，打印该类对象就显示 国家名 即可
"""


class Country(object):

    def __init__(self, name, area):
        self.name = name
        self.area = area

    def __str__(self):
        return self.name


if __name__ == '__main__':
    country1 = Country('China', 'Asia')
    print(country1)

# China
