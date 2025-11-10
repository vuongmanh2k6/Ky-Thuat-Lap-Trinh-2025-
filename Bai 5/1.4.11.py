import numpy as np

# Tạo mảng dữ liệu có cấu trúc
data_type = [('name', 'U10'), ('class', 'i4'), ('height', 'f4')]
students = np.array([
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.1),
    ('Pit', 5, 40.1)
], dtype=data_type)

# Sắp xếp theo 'class', sau đó theo 'height'
sorted_students = np.sort(students, order=['class', 'height'])

print("Kết quả sắp xếp:")
print(sorted_students)
