# 多值参数 一个 * 表示元组，函数的形参通常表示为 *args
# 两个 * 表示字典，函数的形参通常表示为 **kwargs
def sum_numbers(*args):

    num = 0
    print(args)

    # 累加求和 —— 循环遍历
    for n in args:
        num += n

    return num

result = sum_numbers(1,2,3,4,5,6,7)
print(result)