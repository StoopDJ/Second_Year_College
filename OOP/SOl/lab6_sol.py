# Lab Test solution
# Adapted from Python lab by S. Hensman
# author: B. Schoen-Phelan
# date: 03 Nov 2019

class HappyNumbers:
    def __init__(self):
        my_number = int(input("Enter a number: "))
        self.print_all_happy(my_number)

    def sum_squares_digit(self, n):
        sum_sq = 0
        for d in str(n):
            sum_sq = sum_sq + int(d)*int(d)
        return sum_sq

    def check_happy(self, n):
        n1 = n
        while n1!=1 and n1!=4:
            n1 = self.sum_squares_digit(n1)
            # print(n1)
        if n1==1:
            print(n, end=' ')
            # , " is happy")
        # else:
       #     print(n, " is NOT happy")

    def print_all_happy(self, n):
        n1 = n+1
        print("All happy numbers up to",n,"are:")
        for i in range(1,n1):
            self.check_happy(i)
    # else:
    #     print(n, " is NOT happy")

hn = HappyNumbers()


