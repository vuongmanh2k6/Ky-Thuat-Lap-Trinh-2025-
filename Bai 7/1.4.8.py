def write_list_to_file(file_path, data_list):
    with open(file_path, "w", encoding="utf-8") as f:
        for item in data_list:
            f.write(str(item) + "\n")

my_list = ["Python", "Java", "C++", "AI", "Machine Learning"]
write_list_to_file("C:/Users/Vuong Duc Manh/Documents/a.txt", my_list)
