# Nhập danh sách các số, cách nhau bởi dấu phẩy
ds = input("Nhập danh sách số (ngăn cách bằng dấu phẩy): ").split(',')

# Chuyển sang kiểu int và lọc các số lẻ
le = [int(x) for x in ds if int(x) % 2 != 0]

# In kết quả
print("Các số lẻ là:", le)
