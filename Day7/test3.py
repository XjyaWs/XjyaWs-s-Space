class Test(object):
    name = 'a'

test1 = Test()
setattr(test1, 'name', 'b')
setattr(test1, 'age', 15)
print(test1.age)