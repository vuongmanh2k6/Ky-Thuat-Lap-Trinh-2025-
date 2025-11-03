# Nhập một dòng gồm các phần tử, cách nhau bằng dấu cách hoặc tab
ds = input("Nhập danh sách: ").split()

# In ra danh sách vừa nhập
print("Danh sách vừa nhập là:", ds)

# Nếu muốn in từng phần tử trên một dòng:
print("Các phần tử trong danh sách:")
for x in ds:
    print(x)
