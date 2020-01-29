xiaoming_dict = {"name":"小明"}

# 1、取值
print(xiaoming_dict["name"])
# print(xiaoming_dict["123name"])

# 2、增加 / 修改
# 如果 key 不存在，会增加键值对
xiaoming_dict["age"] = 18
# 如果 key 存在，则修改已存在的键值对
xiaoming_dict["name"] = "小明明"

# 3、删除
xiaoming_dict.pop("name")

print(xiaoming_dict)