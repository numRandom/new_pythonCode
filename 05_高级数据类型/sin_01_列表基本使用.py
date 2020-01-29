name_list = ["zhangsan","lisi","wangwu"]

# 1、取值
# 2、列表索引报错 —— list index out of range
print(name_list[1])

# 2、取索引
# 知道 index 数据的内容，想确定数据在列表中的位置，列表.index(self,数据)
# 使用index 方法需要注意，如果传递的数据不在列表中，程序会报错
print(name_list.index("lisi"))

# 3、修改
# list assignment index out of rang 列表指定的索引超出范围
name_list[1] = "李四"
# name_list[3] = "wa"

# 4、增加
# name_list.append()可以在列表的末尾追加数据
name_list.append("wpp")
# inset 可以在列表指定位置添加数据
name_list.insert(1,"bts")
# 在列表的末尾增加一个数据
tmp = ["yy","sope"]
name_list.extend(tmp)

# 5、删除
# remove 删除列表中指定的第一个数据
name_list.remove("zhangsan")
# pop 默认删除列表的最后一个数据
print(name_list.pop())
# 可以在括号中指定某个下标，使pop删除指定的下标，pop 方法会返回删除的数据
print(name_list.pop(0))
# 删除指定位置的数据，不建议使用该关键字
del name_list[0]
# clear
name_list.clear()


print(name_list)