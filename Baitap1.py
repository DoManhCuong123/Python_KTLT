import Baitap2
from decimal import *
a, b = input("Xin moi nhập số a và b:").split()
getcontext().prec = 4
tong = int(a) + int(b)
hieu = int(a) + int(b)
thuong = Decimal(a)/Decimal(b)
tich = int(a) * int(b)
print(a, "+", b, "=", tong)
print(a, "-", b, "=", hieu)
print(a, "/", b, "=", thuong)
print(a, "*", b, "=", tich)
