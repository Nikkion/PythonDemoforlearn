#定义公共变量
goods =['php','js','python','java','ruby','go',]
price=[1000,2000,1500,3000,200,6000]
num = 0
history=[]#记录已购买列表
kind = 0 #记录状态
'''
判定输入的金额是否为整数，不为整数则重新输入
'''
flag=True
while flag:
    salary = input(u"请输入你的金额：")
    if salary.isdigit()==True:
        flag=False
        #以下方法可用迭代器完成
        if salary == '离开':
            print("你没有购买任何商品")
            exit()
        else:
            i = 0
            while i < len(goods):
                print(i, goods[i], price[i])
                i += 1
            salary = int(salary)
            break
    if salary.isdigit()==False:print ("您输入的金额格式有误")

'''
完成第一步金额的录入后，对购买的场景进行分类编写
使用循环嵌套完成
'''
while True:
    if kind == 1:
        print('已买如下产品')
        j = 0
        while j < len(history):
            print(history[j])
            j += 1
        print('还剩余： ', salary,'元')
        exit()
    else:
        buy = input("请选择你需要的商品:")

        if buy == "离开":
            kind = 1
            continue
        elif buy.isdigit():
            buy = int(buy)
            if buy < goods.__len__() and buy >= 0:
                if salary >= price[buy]:
                    history.insert(num, goods[buy])
                    salary = salary - price[buy]
                    num = num + 1
                else:
                    print("你没有足够的钱")
                    continue
            else:
                print("没有这个商品编号")
                continue
        else:
            if buy in goods:
                if salary < price[goods.index(buy)]:
                    print("你没有足够的钱")
                    continue
                else:
                    salary = salary - price[goods.index(buy)]
                    history.insert(num, buy)
                    num = num + 1
            else:
                print("没有这个商品")
                continue






