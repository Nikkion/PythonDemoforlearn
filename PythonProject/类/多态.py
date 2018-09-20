class Animal():
    def __init__(self,name):
        self.name=name
    def talk(self):
        pass

    #多态实现，一个接口实现多个实现
    @staticmethod
    def animal_talk(obj):
        obj.talk()



class Dog(Animal):
    def talk(self):
        print("wang wang wang")

class Cat(Animal):
    def talk(self):
        print("miao miao miao")

d = Dog("哈士奇")
c = Cat("家猫")

# 调用多态，实现多个实现
Animal.animal_talk(d)
Animal.animal_talk(c)

