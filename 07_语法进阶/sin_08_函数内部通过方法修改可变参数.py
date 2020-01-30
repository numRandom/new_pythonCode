def demo(num_list):

    print("函数内部的代码")

    num_list.append(9) # 注意在函数内部，参数在调用方法时，没有智能提示
    print(num_list)

    print("函数执行完成")

gl_list = [1,2,3]
demo(gl_list)
print(gl_list)