n = int(input("整數n:"))
print("數列{0}" .format(n),end=" ")
while(True):
    if n == 1:
        break
    elif n % 2 == 0:
        n /= 2
        print(int(n),end=" ")
    else:
        n = 3 * n + 1
        print(int(n),end=" ")
print()
