# 判断空格（包括空格、\r \n \t）
# 1、判断空格字符
space_str = "   \n\t\r"

print(space_str.isspace())

# 2、判断字符串中是否只包含数字
# 1> 都不能判断小数
# 2> unicode 字符串
# 3> 中文数字
# num_str = "1"
# num_str = "\u00b2"
num_str = "一千零一"

print(num_str)
print(num_str.isdecimal()) # 只包含全角数字
print(num_str.isdigit())  # 包含全角、(1)、
print(num_str.isnumeric())  # 还有判断中文数字