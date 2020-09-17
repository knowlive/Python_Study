s=int(input("s: "))
h=s//3600
s=s%3600
m=s//60
s=s%60
print("시간:",h,"분:",m,"초:",s)
