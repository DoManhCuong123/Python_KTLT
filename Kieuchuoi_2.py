#de sua 1 lenh dac biet 
print(r"Haizz,\neu t khong muon choi")

str1 = "Cuong Do"
str2 = " la nhat"
str3 = str1 + str2
str4 = str1*4
print(str3)
print(str4)
#in (gan giong bool)
stra = "Cuong Do la nhat khong ai sanh bang"
strb = "C"
#in co tac dung kiem tra chuoi trong chuoi
strc = strb in stra
print(strc)
print(stra[-1])
#ham len lay ra do dai chuoi
print(len(stra))
#cat chuoi [diem dau - diem cuoi] co the su dung None 
strd = stra[2:len(stra)]
print(strd)
chuoi1 = int("98") + 5
chuoi2 = str(69) + "5"
print(chuoi2)
print(chuoi1)
stra = stra[None : 1] + "0" + stra[3:None]
print(stra)
print(hash(stra))