import unittest
from VigenereCipher import VigenereCipher
# keyword = row
# plaintext = column

class TestCypher(unittest.TestCase):

    #2
    def setUp(self):
        self.cipher = VigenereCipher("BIKE")
    # 1
    def test_encode(self):
        # cipher = VigenereCipher("BIKE")
        encoded = self.cipher.encode("UNIVERSITY")
        self.assertEqual(encoded, "VVSZFZCMUG")

    #2
    # fails at the beginning, because initial solution
    # is hardcoded
    def test_encode_character(self):
        encoded = self.cipher.encode("E")
        self.assertEqual(encoded, "F")

    #3
    def test_encode_spaces(self):
        encoded = self.cipher.encode("WITH SPACES")
        self.assertEqual(encoded, "XQDLTXKGFA")

    #4
    def test_encode_lower_case(self):
        encoded = self.cipher.encode("with spaces")
        self.assertEqual(encoded, "XQDLTXKGFA")

    #5
    # instead of lookup table, we can use a different trick
    # get number value of characters with ord() where A=0 and Z=25
    # add the numbers together
    # take the remainder and mod 26
    # happens on a character by character basis
    def test_combine_characters(self):
        encoded = self.cipher.combine_character("X", "T")
        self.assertEqual(encoded, "Q")

    #6
    # first thing that an encoder will need is
    # replicating the keyword as many times as fits into
    # the length of a plaintext word
    def test_extend_keyword(self):
        extended = self.cipher.extend_keyword(10)
        self.assertEqual(extended, "BIKEBIKEBI")


if __name__ == "__main__":
    unittest.main()