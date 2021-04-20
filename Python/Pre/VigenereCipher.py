# to take a keyword and a plaintext and
# return the cipher text

class VigenereCipher:
    def __init__(self, keyword):
        self.keyword = keyword

    def encode(self, plaintext):
        # return "VVSZFZCMUG"
        cipher = []
        my_plain = plaintext.upper().replace(" ","")
        keyword = self.extend_keyword(len(my_plain))
        for p,k in zip(my_plain, keyword):
            cipher.append(self.combine_character(p,k))

        return "".join(cipher)

    def combine_character(self, plain, keyword):
        my_plain = plain.upper()
        my_keyword = keyword.upper()
        plain_num = ord(my_plain) - ord('A')
        keyword_num = ord(my_keyword) - ord('A')
        return chr(ord('A')+(plain_num + keyword_num) %26)

    def extend_keyword(self, number):
        repeats = number // len(self.keyword) + 1
        return (self.keyword * repeats)[:number]