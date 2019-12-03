"""
4.定义一个抽象动物 Animal 类(抽象类要设置classmeta)，可以初始化name，age，sex三个属性
有一个对象方法 run 方法，可以输出 "某某在奔跑" ，一个抽象方法 speak 方法(提示import abc @abc.abstractmethod)
"""
import abc


class Animal(metaclass=abc.ABCMeta):

    def __init__(self, name, age, sex):
        self.name = name
        self.age = age
        self.sex = sex

    def run(self):
        print(self.name + '在奔跑')

    @abc.abstractmethod
    def speak(self):
        pass

