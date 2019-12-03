"""
2.定义一个School类，有一个类属性name，值为“学校”，有两个对象属性name，address
初始化两个不同的学校，打印学校对象显示学校名（对象属性name值）即可
"""


class School(object):
    name = "学校"

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def __str__(self):
        return self.name


school1 = School('Oldboy', 'heaven')
school2 = School('Oldgirl', 'hell')
print(school1)
print(school2)

# Oldboy
# Oldgirl
