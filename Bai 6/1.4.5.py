class ReverseWords(object):
    def reverse_words(self, s):
        words = s.split()
        reversed_words = words[::-1]
        return " ".join(reversed_words)

# Test
py_solution = ReverseWords()
print(py_solution.reverse_words("hello .py"))
