# # a
# c = (1,2,3,4,5,6,7,8,9,10)
# for i in range(0,10):
#     print("c(%d):"%i,c[i])
# # b
# solan = 0
# for i in range(0,10):
#     if c[i] % 2 == 0:
#       solan = solan + 1
# print("C có:",solan)
# x = int(input("Xin mời nhập x:"))
# for i in range(0,10):
#       if c[i] == x:
#           print(x,"có trong tuple trên")

#c

a = (12.9,45.8,19.5,27.6)
max = a[0]
for i in range(0,4):
    if a[i] > max:
        max = a[i]
min = a[0]
for i in range(0,4):
    if a[i] < min:
        min = a[i]
print("Min = ", min)

for i in range(0,4):
    if a[i] == 12.0:
        print("Có 12kg trong tupple")
    else: print("Không có 12kg trong tuple")

