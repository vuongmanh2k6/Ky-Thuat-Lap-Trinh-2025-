tong_tien = 0
print("Nhập nhật ký giao dịch (D để gửi, W để rút). Nhập dòng trống để kết thúc:")

while True:
    dong = input()
    if not dong:   # nếu người dùng nhấn Enter mà không nhập gì → dừng
        break
    loai, so_tien = dong.split()
    so_tien = int(so_tien)

    if loai.upper() == 'D':      # gửi tiền
        tong_tien += so_tien
    elif loai.upper() == 'W':    # rút tiền
        tong_tien -= so_tien

print("Số dư cuối cùng là:", tong_tien)
