gia = float(input("Nhập giá sản phẩm: "))
so_luong = int(input("Nhập số lượng mua: "))
tong_chi_phi = gia * so_luong
vat = tong_chi_phi * 0.1
tong_tien = tong_chi_phi + vat
print("Tổng tiền phải trả là:", round(tong_tien, 2))
