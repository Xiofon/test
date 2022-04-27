x = ["金","銀","銅","優"]
n = [0,0,0,0]
for i in range(0,4):
    print(x[i] ,end=" ")
    n[i] = int(input())
for i in range(0,4):
    print("{0}牌得到{1}面" .format(x[i],n[i]))