#a
a = [27,6,2003,"Cường"]
print(a)
#b
b = [2*i for i in range(1,101)]
print(b)
#c
n = int(input("Xin mời nhập số phần tử:"))
c = []
Sum = 0
for i in range(n):
    val = int(input("c[%d]:" %i ))
    c.append(val)
    Sum = Sum + c[i]
print(c)
print(Sum)
#d
# cú pháp format print("tetx %d", %text)
# có thể sử dụng %s và nhiều kiểu khác
# không cần ngoặc giữ câu lệnh và giá trị format
x = int(input("Xin mời nhập n:"))
y = int(input("xin mời nhập m:"))
d = []
for i in range(x):
    d1 = []
    for j in range(y):
        val1 = float(input("d[%d][%d]:" %(i+1,j+1)))
        d1.append(val1)
    d.append(d1)
print(d)