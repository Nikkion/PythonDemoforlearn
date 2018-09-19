import time
class Gun:
    def __init__(self,Newname,allNum,evNum):
        self.__name =Newname
        self.__allNum = allNum
        self.__evNum = evNum

    def biubiu(self):
        if self.__allNum>self.__evNum:
            self.__allNum=self.__allNum-self.__evNum
        else:
            self.__allNum=0
        # print(self.__name+"剩余子弹数量"+self.__allNum)
        print("%s剩余子弹数量%s"%(self.__name,self.__allNum))

Gun1 = Gun("MP5",20,2)
Gun2 = Gun("AK47",50,4)

while True:
    Gun1.biubiu()
    Gun2.biubiu()

    time.sleep(1)

    Gun1.biubiu()
    Gun2.biubiu()

