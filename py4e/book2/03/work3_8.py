a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))

if a<c:
    if a<b:
        print("가장 작은 수: ", a)
    else :
        print("가장 작은 수: ", b)
elif c<a:
    if c<b:
        print("가장 작은 수: ", c)
    else:
        print("가장 작은 수: ", b)
        
