hello_str = "hello world"

# 1、判断是否以指定字符串开始
print(hello_str.startswith("hello"))
print(hello_str.startswith("Hello"))
print("=============================")

# 2、判断是否以指定字符串结束
print(hello_str.endswith("world"))
print("===============================")

# 3、查找指定字符串
# 返回值表示子字符串出现的位置 类同于 index() 方法
# 区别：若不存在子字符串，find()方法返回-1,index() 方法直接报错
# string.find(str,start=0,end=len(string))
print(hello_str.find("llo"))  # 返回值表示子字符串出现的位置 类同于 index() 方法
print(hello_str.find("abc"))
print("=============================")

# 4、替换字符串
# 执行完成后，不会修改原有字符串的内容，只会返回一个新的字符串
print(hello_str.replace("world","2020"))

print(hello_str)