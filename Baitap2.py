from math import *
x1 = float(input("Nhập vào toạ độ x1 của A:"))
y1 = float(input("Nhập vào toạ độ y1 của A:"))
x2 = float(input("Nhập vào toạ độ x2 của B:"))
y2 = float(input("Nhập vào toạ độ y2 của B:"))
A = x1 - x2
B = y1 - y2
d = sqrt(A**2 + B**2)
print("Khoảng cách Euclidean là:", d)
