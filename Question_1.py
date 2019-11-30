def add(n,i):
    return  n+i
def test():
    for i in range(4):
        yield  i
g= test()
# for n in [10000000000,10000000,10]:
#     print(n)
#     g=(add(n,i) for i in g)
# print(list(g))
g=(add(10,i) for i in g)
g=(add(10,i) for i in g)
for i in g:
    print(i)

#生成器问题
# 使用for循环，两次循环都是带入n=10是为什么？