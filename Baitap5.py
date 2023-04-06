n = int(input("Xin mời nhập số nguyên n:"))
if n >= 0 and n < 2:
    print(n, "không phải là số nguyên tố")
else:
    for i in range(2, n):
        if n % i == 0:
            print(n,"không phải là số nguyên tố")
            break
        else:
            print(n,"là số nguyên tố")
            break

