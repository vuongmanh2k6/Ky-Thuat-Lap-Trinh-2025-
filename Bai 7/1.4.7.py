def count_lines(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return len(f.readlines())

print(count_lines("C:/Users/Vuong Duc Manh/Documents/a.txt"))
