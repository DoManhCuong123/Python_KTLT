from math import *
a = float(input("Xin mời nhập số a:"))
b = float(input("Xin mời nhập số b:"))
c = float(input("Xin mời nhập số c:"))
delta = b**2 - 4*a*c
if a == 0:
    print("x", "=", -c/b)
elif a != 0:
    if delta == 0:
        print("x", "=", -b/2*a)
    elif delta < 0:
        print("Phương trình vô nghiệm!")
    else:
        x1 = (-b+sqrt(delta))/(2*a)
        x2 = (-b-sqrt(delta))/(2*a)
        print("x1", "=", x1)
        print("x2", "=", x2)
