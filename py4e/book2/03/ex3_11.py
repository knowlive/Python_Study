a=int(input("a: "))
b=int(input("b: "))
c=int(input("c: "))

if a>b:
    if a>c:
        print("가장 큰 수:", a)
    else:
        print("가장 큰 수:", c)
elif a<b:
    if b>c:
        print("가장 큰 수:", b)
    else:
        print("가장 큰 수:", c)
else:
    print("a랑 b가 같습니다.")
