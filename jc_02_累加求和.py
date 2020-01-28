# 1、定义一个整数变量记录循环的次数
i = 0

# 2、开始循环
sum = 0
while i <= 100:
    sum += i
    i += 1

print(" i 的值为 %d " %i)
print(" 0~100 之间累加的结果为：%d" % sum)