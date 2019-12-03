"""
7.定义一个鸟 Bird 类，继承动物类，可以初始化name，age，sex，type(品种就是字符串类型)四个属性，
重写 run 方法，可以打印 "某某翱翔与天空"，实现 speak 抽象方法，打印 "说鸟语"，
一个对象方法 get_type，打印该鸟得品种
"""
import advanced_ex4


class Bird(advanced_ex4.Animal):

    def __init__(self, name ,age, sex, type: str):
        super().__init__(name, age, sex)
        self.type = type

    def run(self):
        print(self.name + '翱翔与天空')

    def speak(self):
        print("说鸟语")

    def get_type(self):
        print(self.type)


if __name__ == '__main__':
    bird1 = Bird('瑞秋', 1, 'female', '金丝雀')
    bird1.run()
    bird1.speak()
    bird1.get_type()

# 瑞秋翱翔与天空
# 说鸟语
# 金丝雀
