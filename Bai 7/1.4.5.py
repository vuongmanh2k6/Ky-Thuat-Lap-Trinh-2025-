def file_read(fname):
    with open(fname, "a", encoding="utf-8") as myfile:
        myfile.write("Python Exercises\n")
        myfile.write("Java Exercises\n")

    # Đọc lại nội dung tệp và in ra
    with open(fname, "r", encoding="utf-8") as txt:
        print(txt.read())

file_read("C:/Users/Vuong Duc Manh/Documents/a.txt")
