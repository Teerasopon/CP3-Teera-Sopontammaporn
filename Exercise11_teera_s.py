x = int(input("please input times : "))
space = ""
for y in range(x):
    text = "*"
    space = (x-y-1)*" "
    for z in range(y):
        text = text + "**"
    print(space+text)