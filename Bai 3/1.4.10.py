import math

def Tinh(R):
    # Kiểm tra R có phải là số dương hay không
    if R <= 0:
        return "Bán kính không hợp lệ. Vui lòng nhập số dương."
    else:
        chu_vi = 2 * math.pi * R
        dien_tich = math.pi * R**2
        return chu_vi, dien_tich

# Nhập bán kính từ bàn phím
try:
    R = float(input("Nhập bán kính hình tròn: "))
    ket_qua = Tinh(R)
    if isinstance(ket_qua, str):
        print(ket_qua)
    else:
        chu_vi, dien_tich = ket_qua
        print(f"Chu vi hình tròn là: {chu_vi:.2f}")
        print(f"Diện tích hình tròn là: {dien_tich:.2f}")
except ValueError:
    print("Giá trị nhập không hợp lệ. Vui lòng nhập số.")

# Giải thích:
# Hàm Tinh(R) kiểm tra xem R có lớn hơn 0 không (bán kính phải dương).
# Nếu hợp lệ thì tính chu vi = 2πR và diện tích = πR².
# Sử dụng math.pi cho giá trị π chính xác.
# Dùng try-except để xử lý lỗi nhập dữ liệu.
