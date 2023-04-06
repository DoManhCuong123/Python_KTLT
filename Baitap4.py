n = int(input("Xin mời nhập số nguyên n:"))
while not (n >= 20 and n <= 30):
    n = int(input("Xin mời nhập số nguyên n:"))
x = float(input("Xin moi nhập số thực x:"))
P = 2022*(x**n)
for i in range(1, n):
    P = P + i/(x**i)
print("P", "=", P)

