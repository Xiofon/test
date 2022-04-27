import string
while(True):
    x = str(input("檢測的字串(end 結束):"))
    if x == "end":
        break
    a = str(input("檢測的單一字元:"))
    ans = 0
    for i in range(0,len(x)):
        if  x[i] == a :
            ans += 1
    print("字元{0}出現次數為:{1}" .format(a,ans))