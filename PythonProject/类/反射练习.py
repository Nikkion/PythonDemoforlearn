class Dog():
    def __init__(self,name):
        self.name= name
    def eat(self,food):
        print("%s is eatting" % self.name, food)


def buik(self):
    print("%s is yelling...." % self.name)



D = Dog("哈士奇")
choice = input(">>:").strip()

# print(hasattr(D,choice))
# getattr(D,choice)()
"""
反射
    hasattr（obj,name_str）,判断一个对象obj里是否有对应的name_str字符串的方法
    getattr(obj,name_str),根据字符串去获取obj对象里的对应的方法的内存地址。
    setattr(x,y,x)
"""

if hasattr(D,choice):
    fun = getattr(D,choice)
    fun("shit")
else:
    setattr(D, choice, buik)

# if hasattr(D,choice):
#     func = getattr(D,choice)
#     func("shit")
# else:
#     setattr(D, choice, bulk)
#     D.talk(D)
# if hasattr(D,choice):
#     attr= getattr(D, choice)
#     setattr(D, choice, "cheng")
# else:
#     setattr(D, choice, 22)
#     print(getattr(D, choice))
# print(D.name)
if hasattr(D, choice):
    delattr(D, choice)
D.name