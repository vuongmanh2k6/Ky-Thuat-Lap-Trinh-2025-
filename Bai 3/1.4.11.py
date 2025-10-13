def benefit(t, n, k):
    # t: lãi suất % mỗi tháng
    # n: số vốn ban đầu
    # k: số tháng gửi
    # Công thức tính lãi kép: A = n * (1 + t/100)^k
    return n * (1 + t/100)**k

try:
    t = float(input("Nhập lãi suất tiết kiệm (% mỗi tháng): "))
    n = float(input("Nhập số vốn ban đầu: "))
    k = int(input("Nhập số tháng gửi: "))

    tien_nhan_duoc = benefit(t, n, k)
    print(f"Số tiền nhận được sau {k} tháng là: {tien_nhan_duoc:.2f}")
except ValueError:
    print("Dữ liệu nhập không hợp lệ. Vui lòng nhập số hợp lệ.")

# Giải thích:
# Lãi suất tính theo kiểu lãi kép, mỗi tháng lãi được cộng dồn vào vốn.
# Công thức: Số tiền cuối cùng = vốn ban đầu * (1 + lãi suất tháng)^số tháng.
# Hàm benefit nhận lãi suất t (%), vốn n, tháng gửi k và trả về kết quả.
