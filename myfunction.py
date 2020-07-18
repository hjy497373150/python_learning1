def MyFirstFunc():
    print("这是我创建的第一个函数")


def MySecondFunc(name):
    print(name + "大帅比！")

def docfunc(name):
    '函数定义过程的name叫做形参'
    print("传递进来的" + name + "叫做实参.")

MyFirstFunc()
MySecondFunc("胡晋源")
print(docfunc.__doc__)
help(docfunc)

