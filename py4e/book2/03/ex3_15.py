charge=5000
age = int(input("나이:"))
if age<8:
    print("가격: ", charge-5000)
elif age<60:
    print("가격: ", charge)
elif age>=60:
    print("가격: ", charge/2)
