# -*- coding: utf-8 -*-

namelist =[]

def adds():
    name = input("请输入姓名：")
    addr = input("请输入籍贯：")

    tempInfo = {}

    tempInfo["name"] = name
    tempInfo["addr"] = addr

    findFlag = 0
    for tempInfo in namelist:
        if tempInfo['name']== name:
            findFlag=1
            break
    if findFlag==0:
        namelist.append(tempInfo)
def shanchu():
    if len(namelist) <= 0:
        print("*" * 10)
        print("当前系统中没有任何学生信息")
        print("*" * 10)

        # 先提示有哪些用户
    i = 0
    for info in namelist:
        print(i, info['name'], info['addr'])
        i += 1
        # 让用户选择要删除的信息
        delNum = int(input("请数入需要删除的学生信息序号："))
        if delNum < len(namelist) and delNum >= 0:
            del namelist[delNum]

while True:
    #1.输出功能选项
    print("—"*30)
    print("欢迎来到学生管理系统-python")
    print("(1)新增学生信息")
    print("(2)删除学生信息")
    print("(3)修改学生信息")
    print("(4)查询学生信息")
    print("(5)退出系统")
    print("—"*30)


    optionNum = int(input("请进行选择（数字）："))

    #2.等待用户进行选择
    if optionNum == 1:
        adds()
        # 提示用户就输入学生的名字并获取
        # 添加到系统之中
        # name = input("请输入姓名：")
        # addr = input("请输入籍贯：")
        #
        # tempInfo = {}
        #
        # tempInfo["name"] = name
        # tempInfo["addr"] = addr
        #
        # namelist.append(tempInfo)
        # print(namelist)
    elif optionNum == 2:
        shanchu()

    elif optionNum == 3:
        if len(namelist)<=0:
            print("*"*10)
            print("系统中没有学生信息")
            print("*"*10)


        i = 0
        for info in namelist:
            print(i, info['name'], info['addr'])
            i += 1
        modifyNum = int(input("请数入需要修改的学生信息序号："))
        name = input("请输入新的姓名：")
        addr = input("请输入新的籍贯：")

        tempInfo = {}

        tempInfo["name"] = name
        tempInfo["addr"] = addr

        namelist[modifyNum]=tempInfo

    elif optionNum == 4:
        name = input("请输入你需要查询的学生姓名")
        for info in namelist:
            if info['name']==name:
                print("恭喜你，找到了")
            else:
                print("很抱歉，没有找到")


    elif optionNum == 5:
        break