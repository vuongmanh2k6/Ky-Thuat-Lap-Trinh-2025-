def pascal(n):
    tamgiac = []
    for i in range(n):
        hang = [1] * (i + 1)
        for j in range(1, i):
            hang[j] = tamgiac[i - 1][j - 1] + tamgiac[i - 1][j]
        tamgiac.append(hang)
    return tamgiac

n = int(input("Nhập số dòng n: "))
for row in pascal(n):
    print(row)
