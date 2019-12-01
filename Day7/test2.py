class Test:
    test_var = []
    def __init__(self,n):
        self.test_var.append(n)

test1 = Test(100)
print(id(test1.test_var))
print(id(Test.test_var))