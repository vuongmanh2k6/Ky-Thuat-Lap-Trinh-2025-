# Khởi tạo 2 số Fibonacci đầu tiên
a, b = 1, 2
total = 0

print("Dãy Fibonacci nhỏ hơn 4.000.000:")

# Duyệt dãy Fibonacci đến khi vượt quá 4.000.000
while a < 4000000:
    print(a, end=" ")

    # Nếu a là số chẵn thì cộng vào tổng
    if a % 2 == 0:
        total += a

    # Cập nhật a, b cho vòng lặp tiếp theo
    a, b = b, a + b

# In tổng các số chẵn
print("\nTổng các số chẵn trong dãy Fibonacci:", total)
