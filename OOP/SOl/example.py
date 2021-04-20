class Fish:
    def __init__(self, colour='', height=0):
        self.colour = colour
        self.height = height
        self.speed = 0

    def move(self, moved):
        if moved == 'Swim':
            self.speed = 3
            print("Swimming at %d times speed" % (self.speed))
        elif moved == 'trot':
            self.speed = 1 * 2 #1 just to illustrate that we are not at 0 speed anymore
            print("Trotting at %d times speed" % (self.speed))
        elif moved == 'gallop':
            self.speed = 1 * 3 #same as above re speed, just to make it clearer
            print("Galloping at %d times speed" % (self.speed))
        else:
            print('no such value for horse gait')


class Pegasus(Fish):
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
            print('%s in the air!'%(moved))


class MrEd(Fish):
    def chat(self):
        print("I am Mr Ed and I talk")


f = Fish('black', 160)
p = Pegasus('white', 180, 0)
m = MrEd('fawn', 150)

f.move('trot')
f.move('Swim')
f.move('gallop')
# #
p.move(200)
p.move('trot')
#
m.move('Swim')
m.chat()

#should not work as MrEd doesn't fly:
# m.move(300)
# should not work as Horses generally don't fly:
# h.move(200)

