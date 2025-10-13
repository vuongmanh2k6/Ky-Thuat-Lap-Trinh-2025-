a = "Hello Guy!"

def say():
    global a
    a= "Vinh University" 
    print(a)
    
say()
print(a)

# Giải thích:
# Ban đầu, biến a có giá trị "Hello Guy!" (biến toàn cục – global variable).
# Trong hàm say(), ta dùng từ khóa global a.
# → Điều này có nghĩa: “Biến a bên trong hàm chính là biến toàn cục, không phải tạo mới.”
# Sau đó, gán lại a = "Vinh University" → giá trị của biến toàn cục bị thay đổi.
# Khi print(a) trong hàm → in ra "Vinh University".
# Khi print(a) ngoài hàm → cũng in ra "Vinh University" vì giá trị đã bị đổi.
