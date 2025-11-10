import numpy as np

# Dữ liệu đầu vào
student_id = np.array([1023, 5202, 6230, 1617, 1682, 5241, 4532])
student_height = np.array([40.0, 42.0, 45.0, 41.0, 38.0, 40.0, 42.0])

# Sắp xếp nhiều cột (chiều cao, sau đó mã sinh viên)
# np.lexsort() sắp xếp theo thứ tự ngược của tuple (nên để id trước, height sau)
index = np.lexsort((student_id, student_height))

print("Chỉ số sắp xếp:")
print(index)

print("\nDữ liệu sắp xếp:")
for i in index:
    print(student_id[i], student_height[i])
