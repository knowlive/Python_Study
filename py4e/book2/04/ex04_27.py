n1 = int(input("정수1: "))
n2 = int(input("정수2: "))
for i in range(1, n1+1):
    if n1%i==0 and n2%i==0:
        print(i, end=" ")
