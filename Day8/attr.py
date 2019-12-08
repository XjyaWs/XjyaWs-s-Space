class Test(object):
    def test(self):
        print('test')


test1 = Test()
if hasattr(test1, 'test'):
    res = getattr(test1, 'test')   # 反射调用test
    res()