def copy_file(source, destination):
    with open(source, "r", encoding="utf-8") as fsrc:
        with open(destination, "w", encoding="utf-8") as fdst:
            fdst.write(fsrc.read())

copy_file(
    "C:/Users/Vuong Duc Manh/Documents/a.txt",
    "C:/Users/Vuong Duc Manh/Documents/a_copy.txt"
)
