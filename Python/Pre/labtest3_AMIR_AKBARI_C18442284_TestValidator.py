import unittest
from labtest3_AMIR_AKBARI_C18442284_PassValidator import TestValidator


class Test_validator (unittest.TestCase):


    def setUp(self):
        self.valid = TestValidator("BIKE")
    #1
    def test_empty (self):
        encoded = self.Validator.encode("EMPTY")
        self.assertEqual(encoded , " ")
    #2
    def test_spaces(self):
        encoded = self.Validator.encode("WITH SPACES")
        self.assertEqual(encoded, "BIKE !")
    #3
    # fails at the beginning, because initial solution
    def test_character(self):
        encoded = self.Validator.encode("B")
        self.assertEqual(encoded, "C")
    #4
    def test_Number (self):
        encoded = self.Validator.encode("2")
        self.assertEqual(encoded , "4")

    #5
    def test_encode_lower_case (self):
        encoded = self.Validator.encode("with spaces")
        self.assertEqual(encoded , "bike !")

    #6
    def test_Punctuation (self):
        encoded = self.Validator.encode("punctuation")
        self.assertEqual(encoded , "punctuation")
    #7
    def test_sum_values (self):
        sum = self.Validator.encode("LARGEPASSWORD")
        self.assertEqual(sum, "LARGEPASSWORD" )
        print("the ASCII value of LARGEPASSWORD is ",ord("LARGEPASSWORD"))











if __name__ == "__main__":
    unittest.main()
