class RomanToInteger(object):
    def __init__(self):
        # Bảng giá trị La Mã
        self.rom_val = {
            'M': 1000,
            'D': 500,
            'C': 100,
            'L': 50,
            'X': 10,
            'V': 5,
            'I': 1
        }

    def roman_to_int(self, s):
        m_val = 0
        prev = 0
        # Duyệt từ phải sang trái
        for ch in reversed(s):
            cur = self.rom_val[ch]
            if cur < prev:
                m_val -= cur
            else:
                m_val += cur
            prev = cur
        return m_val

# Test
py_solution = RomanToInteger()
print(py_solution.roman_to_int("MMMCMLXXXVI"))  # Ví dụ trong flowchart
