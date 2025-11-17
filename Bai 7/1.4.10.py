def longest_words(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        words = f.read().split()

    if not words:
        return []

    max_length = max(len(word) for word in words)
    return [word for word in words if len(word) == max_length]

print(longest_words("C:/Users/Vuong Duc Manh/Documents/a.txt"))
