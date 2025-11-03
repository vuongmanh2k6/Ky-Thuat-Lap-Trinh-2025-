s = input("Nhập câu: ")
chu_cai = sum(ch.isalpha() for ch in s)
chu_so = sum(ch.isdigit() for ch in s)

print("Số chữ cái là:", chu_cai)
print("Số chữ số là:", chu_so)
