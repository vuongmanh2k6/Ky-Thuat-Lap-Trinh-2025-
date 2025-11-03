# Nhập dãy các từ
ds = input("Nhập dãy các từ: ").split()

# Tìm độ dài lớn nhất
max_len = max(len(tu) for tu in ds)

# Lấy tất cả các từ có độ dài lớn nhất
tu_dai_nhat = [tu for tu in ds if len(tu) == max_len]

# In kết quả
print("Độ dài lớn nhất là:", max_len)
print("Các từ dài nhất là:")
for tu in tu_dai_nhat:
    print(tu)
