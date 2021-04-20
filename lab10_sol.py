# solution for lab on testing
# author: B. Schoen-Phelan
# date: 29-11-2019
import unittest
from lab2fortest import Types_and_Strings

class TestMyStrings(unittest.TestCase):
    def setUp(self):
        self.ts = Types_and_Strings()
        self.value = "HALLO"

    def test_last(self):
        result = self.ts.return_last_char(self.value)
        self.assertEqual(result, self.value[-1])

    def test_lower(self):
        result = self.ts.all_lower(self.value)
        self.assertEqual(result, self.value.lower())

    def test_no_str(self):
        value = 123
        result = self.ts.return_first_char(value)
        self.assertTrue(result is str) # not a good way of checking!
        # breaks the test logic

    def test_ass_no_str(self):
        value = 123
        self.assertRaises(TypeError, self.ts.return_first_char, value)


if __name__ == "__main__":
    unittest.main()





