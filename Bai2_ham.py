from module2 import * 

a = float(input("Xin mời nhập số tiền USD:"))
b = float(input("Xin mời nhập số tiền EUR:"))
c = float(input("Xin mời nhập số tiền RUB:"))

print("USD-->VND =",doisangUSD(a))
print("EUR-->VND =",doisangEUR(b))
print("RUB-->VND =",doisangRUB(c))

S = cong3sothuc(doisangEUR(b),doisangUSD(a),doisangRUB(c))

print("Tổng số tiền VND là:",S)