def tinhtongsochan(lst):
    tong = 0
    for i in lst:
        if i % 2 ==0:
            tong+=i 
    return tong
input_list = input("Nhập danh sách các số đưỢc cách nhau bằng', ': ")
numbers = list(map(int,input_list.split(', ')))
tongchan = tinhtongsochan(numbers)
print("Tổng các số chẵn trong list là: ", tongchan)

