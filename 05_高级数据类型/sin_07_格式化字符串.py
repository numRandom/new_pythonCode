info_tuple = ("wpp",18,165)

# 格式化字符串后面的（）本质上就是一个元组
print("%s 的年龄是 %d 身高是 %.2f" % info_tuple)

info_str =" %s 的年龄是 %d 身高是 %.2f" % info_tuple

print(type(info_str))