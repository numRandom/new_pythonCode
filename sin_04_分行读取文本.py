file = open("README",encoding="utf-8")

while True:
    text = file.readline()

    if not text:
        break

    print(text,end="")

# text = file.readline()
#
# print(text)

file.close()