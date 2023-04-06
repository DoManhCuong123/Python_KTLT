# kieu set khong cho khai bao 1 list o ben trong 
a = {(1,2,3),1,2,3}
b = {1,2,3,4,5}
print(a)
print(type(a))

x = {1,2,3,4}
y = {5,6,7,8}
i = {(9,8,7,6),4,5}
#phep hop
z = x | y
h = x | i
print(z)
print(type(z))
print(h)
print(type(h))
#phep giao
q = x & y
w = y & i
print(q)
print(w)
# add them 1 phan tu vao trong set
b.add(23)
print(b)
# update them nhieu phan tu
# uu tien them phan tu cua ham update
# khi them phan tu dat ngau nhien do khong co chi so trong set  
# khong the khia bao phan tu trung nhau 
c = {12,45,23,65}
b.update(c)
print(b)
# xoa 1 phan tu dang ton tai
# neu xoa 1 phan tu khong ton tai se bao loi 
b.remove(23)
print(b)
# xoa 1 phan tu neu ton tai
# giong voi remove nhung khong bao loi khi phan tu khong ton tai 
b.discard(59)
print(b)
# Xoa tat ca phan tu 
d = {1,2,3,4}
print(d)
d.clear()
print(d)
# lay ra phan tu ngau nhien 
print(b.pop())
print(b)
