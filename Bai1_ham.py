from math import *
x1 = float(input("Nhập vào toạ độ x1 của A:"))
y1 = float(input("Nhập vào toạ độ y1 của A:"))
x2 = float(input("Nhập vào toạ độ x2 của B:"))
y2 = float(input("Nhập vào toạ độ y2 của B:"))
print("A(", x1, ",", y1, ")")
print("B(", x2, ",", y2, ")")


def tinheuclid(x1, y1, x2, y2):
    A = x1 - x2
    B = y1 - y2
    d = sqrt(A**2 + B**2)
    return d


def sosanh(x1, y1, x2, y2):
    if tinheuclid(0, 0, x2, y2) > tinheuclid(x1, x2, 0, 0):
        print("Khoảng cách từ B bé hơn A")
    else:
        print("Khoảng cách từ A bé hơn B")


def tinhchuvi(x1, y1, x2, y2):
    P = round(tinheuclid(0, 0, x2, y2) + tinheuclid(x1,
              x2, 0, 0) + tinheuclid(x1, y1, x2, y2), 3)
    return P


while True:
    print("""     MENU
    --1:Khoảng cách A - B
    --2:Chu vi tam giác OAB
    --3:So sánh A B:""")
    chon = int(input("Xin mời chọn:"))
    if chon == 1:
        print("Khoảng cách là:", round(tinheuclid(x1, y1, x2, y2), 3))
    elif chon == 2:
        print("Chu vi tam giác là:", tinhchuvi(x1, y1, x2, y2))
    elif chon == 3:
        sosanh(x1, y1, x2, y2)
    else:
        print("Không có lựa chọn trong menu")
