# Nhập chuỗi
s = input("Nhập vào một chuỗi: ")

# Tạo dictionary rỗng để lưu kết quả
char_count = {}

# Duyệt từng ký tự trong chuỗi
for ch in s:
    if ch in char_count:
        char_count[ch] += 1
    else:
        char_count[ch] = 1

# In kết quả
print(char_count)
