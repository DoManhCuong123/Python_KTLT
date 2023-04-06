a = 10
b = 9.6
dia_chi = "Số 55 đường Thanh Niên,phường Ngọc Xuyên"
print(b)
print(type(b))
print(type(dia_chi))
print("Quê quán:" + dia_chi)
x,y,z = 1.9,2.4,9.8
print(x,y,z)
print(type(x))
print(type(y))
print(type(z))

#import thu vien
#thu vien decimal lay toan bo noi dung cua thu vien 
#de su dung kieu du lieu decimal ta phai goi thu vien decimal
#từ thư viên decimal import mọi thứ(*) vào
from decimal import*

#lay toi da 30 chu so bao gom nguyen va thap phan
getcontext().prec = 30
print(Decimal(10)/Decimal(3))
f = 10/3
print(f)
d = 10/Decimal(3)
print(d) 
#chi can 1 phan tu la Decimal thi ca phep tinh la decimal
print(type(d))
#python phân biệt chữ Hoa và thường


