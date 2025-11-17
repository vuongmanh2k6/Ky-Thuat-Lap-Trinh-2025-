class IOString(object):
    def __init__(self):
        self.s = ""

    def get_String(self):
        self.s = input()

    def print_String(self):
        print(self.s.upper())

# Test
str1 = IOString()
str1.get_String()
str1.print_String()
