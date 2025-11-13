luong_cb = float(input("Nhập lương cơ bản: "))
ngay_cong = int(input("Nhập số ngày công: "))

luong_ngay = luong_cb / 22
thuong = 0
phat = 0

if ngay_cong > 22:
    thuong = 0.1 * luong_cb
elif ngay_cong < 22:
    phat = 0.05 * luong_cb

tong_luong = luong_ngay * ngay_cong + thuong - phat
print("Tổng lương thực nhận:", round(tong_luong, 2))
