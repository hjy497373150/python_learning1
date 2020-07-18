def myrecur(n):
    if n == 1:
        return 1
    else:
        return n * myrecur(n-1)
number = int(input("请输入一个正整数："))
result = myrecur(number)
print("%d 的阶乘是 %d!" % (number,result))
