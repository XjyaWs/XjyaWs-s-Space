"""
    D
   / \
  A  B  C
  \ /  /
  Mc
"""

class D:
    def f1(self):
        print('from D')


class A(D):
    pass

class B(D):
    def f1(self):
        print('from B')


class C:
    def f1(self):
        print('from C')

class Mc(A,B,C):
    pass

print(Mc.mro())