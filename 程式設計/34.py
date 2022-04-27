x = int(input("輸入一正整數:"))
if (x % 2 == 0) and (x % 11 == 0) and (x % 5 != 0) and (x % 7 != 0):
    print("{0}為新公倍數?:Yes" .format(x))
else:
    print("{0}為新公倍數?:No" .format(x))