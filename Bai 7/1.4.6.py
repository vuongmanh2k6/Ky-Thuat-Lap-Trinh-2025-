import os

def file_read_from_tail(fname, lines):
    bufsize = 8192
    fsize = os.stat(fname).st_size
    iter = 0
    data = []

    with open(fname, "rb") as f:
        while True:
            iter += 1
            seek_size = min(bufsize * iter, fsize)
            f.seek(fsize - seek_size)
            data.extend(f.readlines())

            if len(data) >= lines or seek_size == fsize:
                for line in data[-lines:]:
                    print(line.decode("utf-8"), end="")
                break

file_read_from_tail("C:/Users/Vuong Duc Manh/Documents/a.txt", 2)
