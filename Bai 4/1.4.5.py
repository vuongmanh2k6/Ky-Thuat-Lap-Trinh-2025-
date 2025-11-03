# Nhập danh sách các từ, cách nhau bằng dấu cách hoặc tab
ds = input("Nhập danh sách các từ: ").split()

# Đảo ngược thứ tự danh sách
ds.reverse()

# In ra các từ theo thứ tự ngược lại
print("Các từ theo thứ tự ngược lại là:")
print(' '.join(ds))
