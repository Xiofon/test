n = int(input("輸入N值:"))
na = []
em = []
for i in range(0,n):
    na.append(str(input("請輸入姓名:")))
    em.append(str(input("請輸入電子郵件:")))
a = str(input("請輸入要查詢電子郵件姓名:"))
for i in range(0,n):
    if a == na[i]:
        print("{0}電子郵件帳號為{1}".format(na[i],em[i]))