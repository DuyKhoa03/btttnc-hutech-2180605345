def kt_so_nguyento(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) +1):
        if n % i ==0:
            return False
    return True
number = int(input("Nhap vao so can kiem tra: "))
if kt_so_nguyento(number):
    print(number, " La so nguyen to")
else:
    print(number," Khong phai la so nguyen to.")