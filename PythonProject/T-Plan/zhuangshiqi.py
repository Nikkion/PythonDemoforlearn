def w1(fun):
        def inner():
            print("正在验证")
            fun()
        return  inner
@w1
def f1():
    print("-----1------")
@w1
def f2():
    print("+++++++2+++++++++")

f1()
f2()

# innterFun = w1(f1)
# innterFun()