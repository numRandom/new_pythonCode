has_ticket = int(input("是否有车票："))

if has_ticket == True:
    print("车票检查通过，进行安检")
    knife_len = float(input("刀的长度："))
    if knife_len <= 20.0:
        print("安检通过，祝您旅途愉快")
    else:
        print("啧啧啧，有危险!")
else:
    print("大哥请先买票")

