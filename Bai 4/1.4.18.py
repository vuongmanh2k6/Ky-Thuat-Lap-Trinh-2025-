n = int(input("Nhập số n: "))
fibo = [0, 1]
while True:
    next_val = fibo[-1] + fibo[-2]
    if next_val >= n:
        break
    fibo.append(next_val)
print("Các số Fibonacci nhỏ hơn", n, "là:")
print(fibo)

