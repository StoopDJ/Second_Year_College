# Code by : Amir Akbari
# Compiler used: PyCharm
# Date: 26th of NOV 2019

#grandparent
#part1( top of the UML )
class MagicalCreature:
    def __init__(self, colour='', height=0):
        self.colour = colour
        self.height = height
        self.speed = 0

#parent
#part2(second part of the UML)
class Horse(MagicalCreature):
    def move(self, moved):
        if moved == 'walk':
            self.speed = 1
            print("Walking at %d times speed" % (self.speed))
        elif moved == 'trot':
            self.speed = 1 * 2 #1 just to illustrate that we are not at 0 speed anymore
            print("Trotting at %d times speed" % (self.speed))
        elif moved == 'gallop':
            self.speed = 1 * 3 #same as above re speed, just to make it clearer
            print("Galloping at %d times speed" % (self.speed))
            # if type(moved) is int:  #also works
        else:
            print('no such value for horse gait')

class cat(MagicalCreature):
    def move1(self, moved):
        if moved == 'walk':
            self.speed = 1
            print("Walking at %d times speed" % (self.speed))
        elif moved == 'eat':
            self.speed = 1 * 2 #1 just to illustrate that we are not at 0 speed anymore
            print("eating at %d times speed" % (self.speed))
        elif moved == 'hide':
            self.speed = 1 * 3 #same as above re speed, just to make it clearer
            print("hiding at %d times speed" % (self.speed))
            # if type(moved) is int:  #also works
        elif moved == 'sleep':
            self.speed = 1 * 3  # same as above re speed, just to make it clearer
            print("sleeping at %d times speed" % (self.speed))
            # if type(moved) is int:  #also works

        else:
            print('no such value for cat gait')


#child
#third part of UML(left side)
class spirit_swiftwind(Horse):

    def __init__(self, colour='', height=0, altitude=0):
        super().__init__(colour, height)
        self.altitude = altitude

    def move(self, moved):
        # if type(moved) is int:  #also works
        if str(moved).isnumeric():
            self.altitude = moved
            print("Flying at %d altitude" % (self.altitude))
        else:
            super().move(moved)
            print('called super\'s move')
            print('%s in the air!'%(moved)

    def chat (self):
        print("I am Spirit and I talk and I am Swiftwind and i talk too")

class ThirtyThirty(Horse):
    def chat ( self ):
        print("I am Thirty Thirty and I talk")

class Starlite(Horse):
    def chat (self):
        print("I am Thirty Thirty and I talk")

#child
#third part of UML(right side)
class Cringer_BattleCat(cat):
    def chat ( self ):
        print("I am Cringer and I talk and also I am Battle cat and i talk too")

class Panthor(cat):
    pass

s = spirit_swiftwind('black', 160)
t = ThirtyThirty('white', 180, 0)\
s1= Starlite('Brown', 150)
#
c = Cringer_BalleCat('gold', 170)
p = Panthor('red', 200)
#
s.move('trot')
s.move('walk')
s.move('gallop')
# #
t.move(200)
t.move('trot')
#
s1.move('walk')
s1.chat()
##
c.move1('walk')
c.move1('eat')
c.move1('hide')
c.move1('sleep')
c.chat1()
#
p.move1('walk')
p.move1('eat')
p.move1('hide')
p.move1('sleep')
#
