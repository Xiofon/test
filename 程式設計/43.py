n = str(input())
z = 0
while(True):
    z += 1
    if n[z] == " ":
        break
a = int(n[0:z])
n = int(n[z+1:len(n)])
print("{0}x**{1}".format(a*n,n-1))