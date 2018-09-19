import os
# h获取制定文件夹中的所有文件名字，存放到一个变量中

moviesName = os.listdir("./movies")



# 2.使用循环的方式一个个对文件名字进行修改
# 需要注意文件的路径
# for temp in moviesName:
#     NewName = "[Nik]"+temp
#     # print(temp)
#     os.rename("./movies/"+temp,"./movies/"+NewName)



# 使用循环的方式一个个对文件进行删除名字修改
for temp in moviesName:
    print(temp)
    num=temp.rfind("]")
    flagNum = num+1
    if flagNum>0:
        NewFilename=temp[flagNum:]
        os.rename("./movies/"+temp,"./movies/"+NewFilename)


