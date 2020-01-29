hello_str = "hello hello"

# 1、统计字符串长度
print(len(hello_str))

# 2、统计某一个子字符串在长字符串中出现的次数
print(hello_str.count("llo"))
print(hello_str.count("ii"))

# 2、某一个字符串出现的位置
print(hello_str.index("lo"))
# print(hello_str.index("io")) # 报错！！！