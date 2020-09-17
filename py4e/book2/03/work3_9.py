m = int(input("첫번째 정수: "))
a = int(input("두번째 정수: "))
if a<m:
    m=a
a = int(input("세번째 정수: "))
if a<m:
    m=a
print("가장 작은 정수: ", m)
