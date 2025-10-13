def add(x, y): # Hàm add nhận hai tham số x và y, trả về tổng của hai số này.
    return x + y
def subtract(x, y): # Hàm subtract trả về hiệu của x và y.
    return x - y
def multiply(x, y): # Hàm multiply trả về tích của hai số.
    return x * y
def divide(x, y): 
    if y == 0:
        return "Lỗi! Không thể chia cho 0."
    else:
        return x / y
    # Hàm divide kiểm tra nếu số chia y là 0 thì trả về thông báo lỗi.
    # Nếu không, trả về kết quả phép chia x / y.
    
print("Chọn phép toán:")
print("1. Cộng")
print("2. Trừ ")
print("3. Nhân")
print("4. Chia")

while True:
    choice = input("Nhập lựa chọn (1/2/3/4) hoặc 'q' để thoát: ")
    if choice == 'q':
        print("Goodbye!")
        break
    # Vòng lặp chạy liên tục cho đến khi người dùng nhập 'q' để thoát.
    # Nếu nhập 'q', in lời chào và kết thúc vòng lặp, thoát chương trình.

    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Nhập số thứ nhất: "))
            num2 = float(input("Nhập số thứ hai: "))
        except ValueError:
            print("Dữ liệu không hợp lệ! Vui lòng nhập số.")
            continue
    # Nếu người dùng nhập một trong các lựa chọn '1', '2', '3', '4' (tức các phép toán hợp lệ) thì tiếp tục.
    # Nhập hai số cần tính.
    # Nếu nhập không phải số (ValueError), chương trình sẽ in thông báo lỗi và quay lại vòng lặp (bắt đầu lại).
    
        if choice == '1':
            print(f"{num1} + {num2} = {add(num1,num2)}")
        elif choice == '2':
            print(f"{num1} - {num2} = {subtract(num1,num2)}")
        elif choice == '3':
            print(f"{num1} * {num2} = {multiply(num1,num2)}")
        elif choice == '4':
            result = divide(num1,num2)
            print(f"{num1} / {num2} = {result}")
     # Nếu là cộng, trừ, nhân thì gọi hàm tương ứng và in kết quả.
     # Nếu là chia, gọi hàm divide, hàm sẽ tự xử lý trường hợp chia cho 0.
     
    else:
        print("Lựa chọn không hợp lệ, vui lòng chọn 1, 2, 3, 4 hoặc 'q' để thoát.")
    # Nếu người dùng nhập ký tự hoặc số không phải trong menu, chương trình sẽ thông báo lỗi và yêu cầu nhập lại.
