# Code by : Amir Akbari
# Compiler used: PyCharm
# Date: 29th of Oct 2019
from typing import Dict, Any


class MuseumMoney():

    def __init__(self):
        self.my_col = self.create_collections()


    def create_collections(self):
        my_col = {}

        try:
            fo = open("MuseumsCollectionsArchives_2015.csv", "r")
        except Exception as e:
            my_col = False
            print("Caught this error: %s" % e.__class__.__name__)
        else:
            for line in fo:
                line = line.split()
                print(line)
                for w in line:
                    self.get_Museum_area(w, my_col)

            fo.close()
            return my_col


    def get_Museum_area (self, amount)
        name_of_area = Queue(maxsize=10)

        return  name_of_area


