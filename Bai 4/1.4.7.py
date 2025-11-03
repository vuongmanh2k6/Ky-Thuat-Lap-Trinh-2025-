# Nhập chuỗi từ bàn phím
s = input("Nhập chuỗi: ")

# Loại bỏ tất cả các chữ số
ket_qua = ''.join(ch for ch in s if not ch.isdigit())

# In chuỗi mới
print("Chuỗi sau khi loại bỏ chữ số là:")
print(ket_qua)
