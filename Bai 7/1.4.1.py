input_file = open('C:/Users/Vuong Duc Manh/Documents/a.txt', 'r')

for line in input_file:
    line = line.strip("\n")
    l = len(line)
    s = ""

    while l >= 1:
        s = s + line[l-1]
        l -= 1

    print(s)

input_file.close()
