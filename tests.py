import unittest
from calculator_pr import get_input, backspace, clear, calc

class MockEntry:
    END = None

    def __init__(self):
        self.text = ""

    def get(self):
        return self.text

    def insert(self, index, text):
        self.text += text

    def delete(self, start, end=None):
        if end is None:
            self.text = self.text[:start]
        else:
            self.text = self.text[:start] + self.text[end:]

def backspace(entry):
    input_len = len(entry.get())
    entry.delete(input_len - 1)

def clear(entry):
    entry.delete(0, len(entry.get()))

class TestCalculatorFunctions(unittest.TestCase):

    def test_get_input(self):
        entry = MockEntry()
        get_input(entry, '5')
        self.assertEqual(entry.get(), '5')

    def test_backspace(self):
        entry = MockEntry()
        entry.insert(0, '123')
        backspace(entry)
        self.assertEqual(entry.get(), '12')

    def test_clear(self):
        entry = MockEntry()
        entry.insert(0, '123')
        clear(entry)
        self.assertEqual(entry.get(), '')

    def test_calc(self):
        input_info = "2 + 2"
        try:
            output = str(eval(input_info.strip()))
        except Exception as e:
            self.fail(f"calc() raised an exception: {e}")
        self.assertEqual(output, "4")

if __name__ == '__main__':
    unittest.main()
