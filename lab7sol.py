# Lab 7 solution
# author: B. Schoen-Phelan
# date: 07 Nov 2019


import string

class WordGames:
    def __init__(self):
        self.my_words = input("Please enter a word or sentence: ")
        self.word_play()

    def word_play(self):
        print("User input was: "+self.my_words)


class WordScramble(WordGames):
    def word_play(self):
        scrambled = ''
        # print('let\'s scramble words')
        list_of_words = self.my_words.split()
        tuple_of_punctuation = (',','.',';','?',' ','!')

        for word in list_of_words:
            # print(word)
            if len(word) > 4:
                if any(p in word for p in string.punctuation): # assuming at end position
                    scrambled += word[0] + word[-2] + word[2:-2] + word[1] + word[-1] +' '
                else:

            # if (len(word) > 4 and word not in string.punctuation):
                #a simple scrambler, uses first, then last, then what's in between, then the second
                    scrambled += word[0] + word[-1] + word[2:-1] + word[1] + ' '
            else:
                print("Too few letters for scrambling")

        print(scrambled)

class WordDupli(WordGames):
    def word_play(self):
        print("User input doubled: ")
        # easy option:
        dupli = self.my_words +' '+self.my_words
        print(dupli)

class DiamondWord(WordScramble, WordDupli):
    pass

# wg = WordGames()
wd = WordDupli()
# ws = WordScramble()
dw = DiamondWord()
# print(DiamondWord.__mro__)

