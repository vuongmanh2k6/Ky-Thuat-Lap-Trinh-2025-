a = "Hello Guy!"

def say(a):
    a= "Vinh University" # Biến cục bộ
    print(a)
    
say(a) # In ra biến cục bộ bên trong hàm
print(a) # In ra biến toàn cục bên ngoài hàm

# Giải thích:
# Biến a toàn cục = "Hello Guy!"
# Trong hàm, khai báo 1 biến a mới (cùng tên nhưng không phải biến toàn cục).
# → Đây là biến cục bộ, chỉ tồn tại trong hàm.
# Khi print(a) trong hàm → in "Vinh University".
# Khi print(a) ngoài hàm → in "Hello Guy!".
