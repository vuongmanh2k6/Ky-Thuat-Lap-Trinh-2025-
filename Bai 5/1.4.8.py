def Sequential_Search(dlist, item):
    pos = 0   # vị trí bắt đầu
    found = False

    while pos < len(dlist) and not found:
        if dlist[pos] == item:
            found = True
        else:
            pos += 1

    return found, pos if found else -1


# --- Chương trình chính ---
dlist = list(map(int, input("Nhập danh sách số, cách nhau bởi dấu cách: ").split()))
item = int(input("Nhập phần tử cần tìm: "))

found, pos = Sequential_Search(dlist, item)

if found:
    print(f"Tìm thấy {item} tại vị trí {pos}")
else:
    print(f"Không tìm thấy {item} trong danh sách.")
