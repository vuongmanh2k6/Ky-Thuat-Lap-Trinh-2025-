def file_read_from_head(fname, nlines):
    from itertools import islice
    with open(fname) as f:
        for line in islice(f, nlines):
            print(line, end="")

file_read_from_head('C:/Users/Vuong Duc Manh/Documents/a.txt', 2)

