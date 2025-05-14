def daonguoclist(lir):
    return lir[::-1]
input_list = input("Mời nhập danh sách các số cách nhau bằng ', ': ")
numbers = list(map(int, input_list.split(', ')))

if input_list is None or input_list == "":
    print("Chuỗi rỗng")
else:
    print("List sau khi đảo ngược là", daonguoclist(input_list))