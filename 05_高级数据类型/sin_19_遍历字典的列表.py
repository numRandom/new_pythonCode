students = [{"name":"小美"},
            {"name":"小明"},
            {"name":"阿土"}
            ]

find_name = "李四"

for stu in students:

    print(stu)

    if stu["name"] == find_name:
        print("找到啦！")
        break

    # else:
    #     print("抱歉没有找着")

else:
    # 如果希望在搜索列表时，所有的字典检查之后，都没有找到需要搜索的目标
    # 还希望得到一个提示，则可以用 完整的for语句 (for else)
    print("顺利遍历完成，但是没有找到")

print("遍历完成")