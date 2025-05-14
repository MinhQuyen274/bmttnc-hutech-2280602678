def daonguocchuoi(chuoi):
    return chuoi[::-1]
input_string = input("Mời nhập chuỗi cần đảo ngược: ")
if input_string is None or input_string == "":
    print("Chuỗi rỗng")
else:
    print("Chuỗi đảo ngược là", daonguocchuoi(input_string))