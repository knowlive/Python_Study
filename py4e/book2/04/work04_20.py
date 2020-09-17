n = int(input("약수를 구할 수: "))
s = 0
for i in range(1, n+1):
    if n%i==0:
        s=s+1
        print(i, end=" ")
print("약수의 갯수: ", s)
