# Nhập khoảng (a, b)
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))

# Kiểm tra điều kiện
if a >= b:
    print("Giá trị a phải nhỏ hơn b!")
else:
    print(f"\nSố nghịch đảo trong khoảng ({a}, {b}):")
    for i in range(a + 1, b):
        print(f"{i} -> 1/{i} = {1/i:.4f}")

