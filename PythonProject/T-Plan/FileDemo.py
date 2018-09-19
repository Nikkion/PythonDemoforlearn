#econding=utf-8
# f = open("1234.txt","r")
# con =f.read()
# print(con)
# # f.write("nihao,hahah")
# f.close()

# 1.提示用户输入需要复制的文件名字：
# 2.打开文件
# 3.读取这个文件
oldfileName = input("请输入要拷贝的文件名字：")
oldfile=open(oldfileName,"r")

# 切割旧文件，组织成新文件
num= oldfileName.find(".")
a1 = oldfileName[0:num]
a2 =oldfileName[num:]

newfileName =a1+"[复件]"+a2
# 打开新文件
newfile=open(newfileName,"w")
content= oldfile.readline()


# 将读取到的文件进行复制
while len(content)>0:
    newfile.write(content)
    content = oldfile.readline()

# 将文件关闭
oldfile.close()
newfile.close()
