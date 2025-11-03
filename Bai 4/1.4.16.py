s = input("Nhập các số nhị phân, cách nhau bởi dấu phẩy: ")
ds = s.split(',')
for b in ds:
    print(int(b, 2))  # chuyển từ nhị phân sang thập phân
