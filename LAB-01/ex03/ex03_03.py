def taotupletulist(lst):
    return tuple(lst)
input_list = input("Nhập danh sách các số, cách nhau bằng ', ': ")
numbers = list(map(int, input_list.split(', ')))
my_tuple = taotupletulist(numbers)
print("List: ", numbers)
print("Tuple từ list: ", my_tuple)