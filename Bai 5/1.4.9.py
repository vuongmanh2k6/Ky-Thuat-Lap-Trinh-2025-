def binary_search(lst, value):
    lower_bound = 0
    upper_bound = len(lst) - 1

    while lower_bound <= upper_bound:
        mid_point = (lower_bound + upper_bound) // 2

        if lst[mid_point] == value:
            return True
        elif lst[mid_point] < value:
            lower_bound = mid_point + 1
        else:
            upper_bound = mid_point - 1

    return False


lst = list(map(int, input("Nhập danh sách (cách nhau bởi dấu cách): ").split()))
value = int(input("Nhập giá trị cần tìm: "))

found = binary_search(lst, value)
print("Kết quả tìm kiếm:", found)
12345678
