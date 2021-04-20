#write a class suberu9921 that has 3 gears, 1, 2 and 3 that have 1.5* the speed of the previous gear, this car can be any colour,
# with either ribbed, or lined wheles, default speed is 0 and gear 1 is set to 50mph
#write a class for suberu9921S that inherits from suberu9921 but instead has 4 gears instead of 3 and each gear gear instead gives 1.4* the speed of the prevous gear.
#write another class for suberu99215T that inherits from suberu9921 that has the same 3 gears as the suberu99215 but each gear increases the speed by 1.6*


class suberu9921:
    def __init__(self, gear_num, color, wheels, class_no = 1):
        self.class_no = class_no
        self.speed = 0
        self.color = color
        self.wheels = wheels
        self.speed_factor = 0

        if self.class_no == 1:
            self.speed_factor = 1.5
        if self.class_no == 2:
            self.speed_factor = 1.4
        if self.class_no == 3:
            self.speed_factor = 1.6

        if gear_num == 1:
            self.speed = 50
        elif gear_num == 2:
            self.speed = 50 * self.speed_factor
        elif gear_num == 3:
            self.speed = 50 * self.speed_factor ** 2

    def get_speed(self):
        print(self.speed)

class suberu9921S(suberu9921):
    def __init__(self, gear_num, color, wheels,class_no = 2):
        super().__init__(gear_num, color, wheels, class_no)
        if gear_num == 4:
            self.speed = 50 * self.speed_factor ** 3

class suberu99215T(suberu9921):
    def __init__(self, gear_num, color, wheels,class_no = 3):
        super().__init__(gear_num, color, wheels, class_no)

o1 = suberu9921(3,"red","stripes")
o2 = suberu9921S(4,"blue","lines")
o3 = suberu99215T(2, "green", "lines")

print(o1.speed, o1.speed_factor)
print(o2.speed, o2.speed_factor)
print(o3.speed, o3.speed_factor)
