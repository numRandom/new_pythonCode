# 在函数中定义缺省参数的默认值时，在函数的形参后边写上 = (默认值)
def print_info(name,gender=True):
    """

    :param name: 同学姓名
    :param gender: True:男生  False:女生
    """

    gender_text = "男生"

    if not gender:
        gender_text = "女生"

    print("%s 是 %s" % (name,gender_text))

print_info("小明")
print_info("小美",False)
