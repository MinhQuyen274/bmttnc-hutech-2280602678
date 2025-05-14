def kiemtrasonguyento(n):
    if n<=1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
number = int(input("Nhập số cần kiểm tra: "))
if kiemtrasonguyento(number):
    print(f"Số {number} là số nguyên tố")
else:
    print(f"Số {number} là không số nguyên tố")
