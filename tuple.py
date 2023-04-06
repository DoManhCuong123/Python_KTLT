# sự khác nhau giữ t và list : tuple không thể thay đổi các phần tử khi được gán - tượng tự như private trong c++
odd1 = ("Cường","Đẹp","Zai")
odd2 = ("Cường","có",5,"tỷ")
odd2 = ("Cường",[1,2,3],(4,5,6))
odd3 = ("Cường",(1,2,3),(4,5,6))
odd4 = ("Cường",[1,2,3],[4,5,6])
# có thể tạo 1 tuple mà không cần dấu ngoặc đơn 
# tuple là bất biến không thay đổi được tuy nhiên lại có thể đổi list bên trong nó 
odd2[1][1] = "Nam" 
print(odd2)
# có thể sử dụng cộng để nối 2 tuple hoặc nhân để lặp lại lúc đó sẽ tạo ra 1 tuple mới 
opp1 = odd1 + odd2
print(opp1)
#opp2 = odd1*odd1
# tuy nhiên chúng ta có thể xoá phần tử trong tuple bằng del 