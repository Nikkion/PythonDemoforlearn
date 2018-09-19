#coding=utf-8
# import random
#
# while True:
#     playerStr = raw_input("请输入 剪刀（0） 石头（1） 布（2）:")
#     player =int(playerStr)
#
#     ubuntu =random.randint(0,2)
#
#     if (player==0 and ubuntu==2)or(player==1 and ubuntu==0) or(player==2 and ubuntu==1):
#         print ('获胜了，很开心')
#     elif player==ubuntu:
#         print ('平均了，不要走，休息一下 接着来')
#
#     else:
#         print ('输了，洗洗手，决战到天亮')

#······································
# i=0
# while i<5:
#     j=0
#     while j<=i:
#         print "*",#加了逗号不会换行
#         j+=1
#     print ""#换行
#     i+=1
#..............................................................................
# class SanjiaoxingArea():
#     def getNums(self):
#         self.__a= input("请输入第一个数：")
#         self.__b= input("请输入第二个数：")
#     def cal(self):
#         print ("矩形的面积为：%d"%(self.__a *self.__b/2.0))
#
#
#
#
# a = SanjiaoxingArea()
# a.getNums()
# a.cal()
#````````````````````````````````````````````````````````````````````

#重写
class Cat:
    def __init__(self,newName,newAge):
        self.__name = newName
        self.__age = newAge
        print ("我是Cat类中构造方法")

class Bosi(Cat):
    def __init__(self):
        print ("我是博士")
bosi = Bosi()