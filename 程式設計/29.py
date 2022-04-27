import string
x = str(input("甲方的數字:"))
y = str(input("乙方的數字:"))
l = len(x)
print("洗刷刷結果:",end = "")
for a in range(0,l):
    if x[a] == "1":
        if y[a] == "5":
            print("贏",end="")
        elif y[a] == "2":
            print("輸",end="")
        else:
            print("和",end="")
    elif x[a] == "2":
        if y[a] == "1":
            print("贏",end="")
        elif y[a] == "3":
            print("輸",end="")
        else:
            print("和",end="")
    elif x[a] == "3":
        if y[a] == "2":
            print("贏",end="")
        elif y[a] == "4":
            print("輸",end="")
        else:
            print("和",end="")
    elif x[a] == "4":
        if y[a] == "3":
            print("贏",end="")
        elif y[a] == "5":
            print("輸",end="")
        else:
            print("和",end="")
    elif x[a] == "5":
        if y[a] == "4":
            print("贏",end="")
        elif y[a] == "1":
            print("輸",end="")
        else:
            print("和",end="")