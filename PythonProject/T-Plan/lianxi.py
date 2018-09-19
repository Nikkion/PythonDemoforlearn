good =['phone','shoes','clothes','headset','apple','computer',]
price=[5000,200,150,2000,2,8000]
money = input("please your wages")
if money == 'out':
    print("You didn't buy anthing and thank for your shopping")
    exit()
else:
    i=0
while i<len(good):
    print(i,good[i],price[i])
    i+=1
num = 0
sc=[]
money=int(money)
key = 0
while True:

    if key == 1:
        print('you have ben bought these goods')
        j=0
        while j < len(sc):
            print(sc[j])
            j += 1
        print('you have ',money,'left')
        exit()
    else:
        buy = input("please choose your goods")

        if buy=="out":
            key = 1
            continue
        elif buy.isdigit():
            buy = int(buy)
            if buy<5 and buy >= 0:
                if money>=price[buy]:
                    sc.insert(num,good[buy])
                    money=money-price[buy]
                    num =num + 1
                else:
                    print("you don't have enough money")
                    continue
            else:
                print("no this goods number")
                continue
        else :
            if buy in good:
                if money < price[good.index(buy)]:
                    print("you don't enough money")
                    continue
                else:
                    money=money-price[good.index(buy)]
                    sc.insert(num, buy)
                    num =num+ 1
            else:
                print("not this good")
                continue