min=int(input("분: "))
day=min//1440
min=min%1440
hour=min//60
min=min%60
print(day, "일", hour, "시간", min, "분")
