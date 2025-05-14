sogiolam = float(input("Nhập số giờ làm mỗi tuần: "))
luong_gio = float(input("Nhập thù lao trên một giờ làm tiêu chuẩn: "))
giotieuchuan = 44
giovuotchuan = max(0, sogiolam - giotieuchuan)
thuclinh = giotieuchuan * luong_gio + giovuotchuan *luong_gio * 1.5
print("Số tiền thực lĩnh của nhân viên là: ", thuclinh)