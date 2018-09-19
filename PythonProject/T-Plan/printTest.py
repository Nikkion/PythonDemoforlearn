# def test(num):
#     if num >=1:
#         res=num*test(num-1)
#     else:
#         res=1
#     return  res
#
# res = test(3)
# print(res)

# ----------------------------------------------------------------
# test =lambda a:a*3.14
# b=3
# c=test(b)
# print(c)

# ------------------------------------------------------------------
# test1 =lambda a,b:a*b
# a=2
# b=3
# c=test1(a,b)
# print(c)
# ---------------------------------------------------------------------

i=1
while i<=9:
    j = 1
    while  j<=i:
        print(j,"*",i,"=",i*j,end=" ")
        j+=1
    print("")
    i+=1

