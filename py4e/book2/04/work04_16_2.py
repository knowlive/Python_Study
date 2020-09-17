a = int(input("1부터 어느 정수까지?: "))
sum = 0
for i in range(1, a+1):
    sum = sum + i
print("1에서",a,"까지의 합은: ", sum)
