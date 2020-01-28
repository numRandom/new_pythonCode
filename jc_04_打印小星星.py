# i = 1
# while i <= 5:
#     print("*" * i)
#     i += 1
#

# print("1", end="")
# print("2",end="")

row = 1

while row <= 5:

    col = 1

    while col <= row:
        print("*",end="")
        col += 1

    print("")
    row += 1