# a
n = int(input("Xin mời nhập số phần tử:"))
a = []
Sum = 0
for i in range(n):
    val = int(input("a[%d]:" % i))
    a.append(val)
# cú pháp hàm copy (hàm cần copy).copy()
x = a.copy()
c = a.copy()
# khi sử dụng hàm sort không được sử dụng trong hàm print
a.sort()
print("Hàm sua khi sắp xếp tăng dần:", a)
# b
max = a[0]
for i in range(1, n):
    if a[i] > max:
        max = a[i]
min = a[0]
for i in range(1, n):
    if a[i] < min:
        min = a[i]
for i in range(n):
    if c[i] % 2 == 0:
        vitri = i
        break
    else:
        vitri = None
print("MAX:", max)
print("MIN:", min)
print("Hàm ban đầu:", c)
print("Vị trí phần tử chẵn đầu tiên:", vitri)
solan = a.count(3)
if solan > 0:
    print("Số 3 có xuất hiện và xuất hiện", solan, "lần")
else:
    print("Số 3 không xuất hiện")
# c
k = int(input("Xin mời nhập vị trí k:"))
y = int(input("Nhập phần tử muốn chèn:"))
a.insert(k,y)
print("Danh sách sau khi thêm:",a)
for i in range(n-1):
    if c[i] % 2 == 0:
        c.remove(c[i])
print("Danh sách sau khi xoá:",c)
# d
m = int(input("Xin mời nhập m phần tử:"))
b = []
for i in range(m):
    val2 = input("a[%i]:"%i)
    b.append(val2)
b.extend(b)
b.reverse()
b.extend(x)
print("Ta có mảng c:",b)


