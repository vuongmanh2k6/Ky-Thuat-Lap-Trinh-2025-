import math

# Nhập hệ số a, b, c từ bàn phím
a = float(input("Nhập a: "))
b = float(input("Nhập b: "))
c = float(input("Nhập c: "))

# Trường hợp phương trình bậc nhất hoặc vô nghiệm
if a == 0:
    if b == 0:
        if c == 0:
            print("Phương trình có vô số nghiệm.")
        else:
            print("Phương trình vô nghiệm.")
    else:
        x = -c / b
        print("Phương trình có một nghiệm: x =", x)
else:
    # Tính delta
    delta = b**2 - 4*a*c
    
    if delta < 0:
        print("Phương trình vô nghiệm thực.")
    elif delta == 0:
        x = -b / (2*a)
        print("Phương trình có nghiệm kép: x₁ = x₂ =", x)
    else:
        x1 = (-b + math.sqrt(delta)) / (2*a)
        x2 = (-b - math.sqrt(delta)) / (2*a)
        print("Phương trình có 2 nghiệm phân biệt:")
        print("x₁ =", x1)
        print("x₂ =", x2)
