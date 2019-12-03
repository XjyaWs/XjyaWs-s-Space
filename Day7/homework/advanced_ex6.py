"""
6.定义一个人 People 类，继承动物类，可以初始化name，age，sex，country(Country类型对象)四个属性，
重写 run 方法，可以打印 "来到公路上" "某某在奔跑"，实现 speak 抽象方法，打印 "说人话"，
一个方法属性(只读属性)，获取自身国家所在的大洲
"""
import advanced_ex4
import advanced_ex5


class People(advanced_ex4.Animal):

    def __init__(self, name, age, sex, country: advanced_ex5.Country):
        super().__init__(name, age, sex)
        self.country = country

    def run(self):
        print("来到公路上, " + self.name + "在奔跑")

    def speak(self):
        print("说人话")

    @property
    def area(self):
        return self.country.area


if __name__ == '__main__':
    country1 = advanced_ex5.Country('China', 'Asia')
    people1 = People('Xiaoming', 18, 'male', country1)
    print(people1.area)

# Asia
