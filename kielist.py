#kiểu danh sách
a = [1,34,5]
b = ["Cuon","hello"]
c = [12,"dasda",149]
#danh sách lồng danh sách
d = [1,2,4,["hello",6,7],9]
#cách truy cấp vào phần ử trong danh sách
print(d[1])
# nếu gọi chỉ số theo chiều dương sẽ bắt đầu từ 0
# nếu gọi chỉ số theo chiều âm sẽ bắt đầu từ -1
print(d[-1])
print(d[3][0])
print(d[-2][-1])
print(d[-2][1])
print(d[-2][0])
# cắt danh sách tron python
# [bắt đầu : kết thúc : bước cắt]
# lưu ý không lấy giá trị kết thúc bên phải
# khi bước lớn hơn , bước thứ n sau bước khi chạy đủ số bước sẽ lấy giá trị tại chỗ dừng
print(d[1:5:2])
print(d[None:None:2])
print(d[:])
# thêm xoá phần tử
odd = [2,45,7,9]
odd[0] = 0
odd[3] = 1
print(odd)
odd[None:2] = [27,6]        
print(odd)
# sử dụng append để thêm 1 phần tử
odd.append(10)
print(odd)
# sử dụng extend để thêm 1 danh sách hay thêm nhiều phần tử vào cuối mảng 
odd.extend([10,8,1])
print(odd)
# sử dụng insert để chèn 1 phần tử vào chỉ số
odd.insert(1,89)
print(odd)
# sử dụng remove để xoá 1 phần tử trong mảng 
odd.remove(odd[1])
print(odd) 
# sử dụng clear để xoá toàn bộ phần tử trong mảng 
odd.clear()
print(odd)
# sử dụng pop để lấy ra phần tử cuối cùng hoặc phần tử có chỉ số truyền vào mảng
odd = [1,2,3,4,5,6,7]
odd.pop() # tương đương với remove
# sử dụng index để trả về chỉ số đầu tiên được tim thấy
# sử dụng count để trả về số lượng phần tử bằng số lượng truyền vào 
# sử dụng sort để sắp xếp mảng tăng dần
# sử dụng reverse để đảo ngược cái vị trí trong mảng
# sử dụng copy để copy danh sách 

