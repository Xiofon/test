ic = [123 , 456,789,321,654]
na = ["Tom" , "Cat" , "Nana" , "Lim" , "Won"]
h = ["DTGD","CSIE","ASIE","DBA","FDD"]
s = int(input("輸入查詢學號:"))
for a in range(0,5):
    if s == ic[a]:
        print("學生資料為:{0} {1} {2}".format(ic[a],na[a],h[a]))
        break
