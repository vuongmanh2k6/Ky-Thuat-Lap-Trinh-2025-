s = input("Nhập câu: ")

chu_hoa = sum(1 for ch in s if ch.isupper())
chu_thuong = sum(1 for ch in s if ch.islower())

print("Chữ hoa:", chu_hoa)
print("Chữ thường:", chu_thuong)
