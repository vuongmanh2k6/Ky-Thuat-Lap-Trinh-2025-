# Nhập list từ bàn phím
lst = list(map(int, input("Nhập các số, cách nhau bởi dấu cách: ").split()))

# Dùng hàm có sẵn
print("Số lớn nhất:", max(lst))
print("Số nhỏ nhất:", min(lst))
