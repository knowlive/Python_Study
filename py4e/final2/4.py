def power(x,y):
    res = x
    for i in range(y-1):
        res*=x
    return res

x=int(input('x= '))
y=int(input('y= '))
result=power(x,y)
print(x, '의 ', y, '제곱= ', result)
