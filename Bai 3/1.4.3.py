def say_hello():
    a = "Hello"
    print(a)
    print(a)
say_hello()

# Nguyên nhân:
# Biến a được khai báo bên trong hàm say_hello(), nên nó chỉ tồn tại trong phạm vi của hàm (biến cục bộ – local).
# Khi gọi print(a) bên ngoài, chương trình không biết a là gì → lỗi.

# Sửa lỗi
# Biến trong hàm (local) không dùng được bên ngoài.
# Muốn dùng bên ngoài thì phải khai báo toàn cục (global).
