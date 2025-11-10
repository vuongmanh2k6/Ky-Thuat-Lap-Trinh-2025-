def bubbleSort(nlist):
    n = len(nlist)
    for i in range(n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if nlist[j] > nlist[j + 1]:
                nlist[j], nlist[j + 1] = nlist[j + 1], nlist[j]
                swapped = True
        if not swapped:
            break
    return nlist

# Nhập dữ liệu từ bàn phím
data = list(map(int, input("Nhập danh sách số, cách nhau bởi dấu cách: ").split()))
sorted_data = bubbleSort(data)
print("Danh sách sau khi sắp xếp:", sorted_data)
