import math

# Vị trí ban đầu tại (0, 0)
pos = [0, 0]

while True:
    s = input()  # Nhập lệnh, ví dụ: UP 5
    if not s:    # Nếu nhập dòng trống → thoát vòng lặp
        break

    movement = s.split()
    direction = movement[0]
    steps = int(movement[1])

    if direction == "UP":
        pos[1] += steps
    elif direction == "DOWN":
        pos[1] -= steps
    elif direction == "LEFT":
        pos[0] -= steps
    elif direction == "RIGHT":
        pos[0] += steps

# Tính khoảng cách từ (0, 0) đến vị trí cuối cùng
distance = int(round(math.sqrt(pos[0]**2 + pos[1]**2)))
print(distance)

# Giải thích:
# Bước	Nội dung	                    Giải thích
# 1	pos = [0, 0]	                Gốc tọa độ (x=0, y=0)
# 2	while True: + input()	        Nhập nhiều lệnh di chuyển cho đến khi người dùng nhấn Enter để kết thúc
# 3	split()	                        Tách chuỗi nhập thành 2 phần: hướng & số bước
# 4	Xử lý UP / DOWN / LEFT / RIGHT	Cập nhật giá trị x, y theo hướng
# 5	math.sqrt(x² + y²)	        Công thức khoảng cách từ (0,0) đến (x,y)
# 6	round() + int()	                Làm tròn kết quả để in ra số nguyên
