# a solution for lab test 2
# author: B. Schoen-Phelan
# date: 25 Nov 2019

class MagicalCreature:
    def __init__(self):
        self._owner = ''
        self._alter_ego_owner = False
        self._alter_ego = False
        self._battle_armour = False
        self._can_talk = True
        self._colour = "white"
        self._can_transform = True
        self._character = "good"

    # setters
    def _set_owner(self, value):
        self._owner = value

    def _set_alter_ego(self, value):
        self._alter_ego = value

    def _set_alter_ego_owner(self, value):
        self._alter_ego_owner = value

    def _set_colour(self, value):
        self._colour = value

    def _set_talkability(self, value):
        self._can_talk = value

    def _set_transformability(self, value):
        self._can_transform = value

    def _set_battle_armour(self, value):
        self._battle_armour = value
        if self._battle_armour:
            print("I'm wearing armour")
        else:
            print("no armour")

    def _set_character(self, value):
        self._character = value

    # getters
    def get_owner(self):
        return self._owner

    def get_alter_ego(self):
        return self._alter_ego

    def get_alter_ego_owner(self):
        return self._alter_ego_owner

    def get_battle_armour(self):
        return self._battle_armour

    def get_transformability(self):
        return self._can_transform

    def get_talkability(self):
        return self._can_talk

    def get_colour(self):
        return self._colour

    def get_character(self):
        return self._character


    # behaviours
    def magic_transform(self, status):
        if self.get_transformability():
            if status == "enhanced":
                if self.get_alter_ego():
                    print("I'm transforming into my alter ego character ", self._alter_ego)
                else:
                    print("transforming without alter ego")
            elif status == "normal":
                print("I'm transforming to normal")
            else:
                print("don't know what to do")
        else:
            print("I don't transform")



    def talk(self):
        if self.get_talkability():
            print("I talk a lot")
        else:
            print("This creature does not talk")


class Horse(MagicalCreature):
    def __init__(self):
        super().__init__()
        self._can_fly = True
        self._has_wings = False # could be unique only to Switfi

    # setters
    def _set_wings(self, value):
        self._has_wings = value

    def _set_flyability(self, value):
        self._can_fly = value

    # getters
    def get_flyability(self):
        return self._can_fly

    def get_wings(self):
        return self._has_wings

    # behaviour
    def neigh(self):
        print("woo hoo hoo")


class Cat(MagicalCreature):
    def __init__(self):
        super().__init__()
        self._many_lives = True

    # getter
    def get_many_lives(self):
        return self._many_lives

    # behaviour
    def purr(self):
        print("meow www rrrr www")

    def scratch_show_claws(self):
        print("scratching")


class SpiritSwiftwind(Horse):
    def __init__(self):
        print("Spirit init")
        self._set_wings(True)
        self._set_owner("Adora")
        self._set_alter_ego_owner("She-Ra")
        self._set_alter_ego("Swiftwind")
        self._set_battle_armour(False)
        self._set_transformability(True)
        self._set_flyability(True)
        self._set_talkability(True)
        self._set_character("good")


    def magic_transform(self, status):
        if status == "enhanced":
            self._set_battle_armour(True)
        elif status == "normal":
            self._set_battle_armour(False)

        super().magic_transform(status)

# s = SpiritSwiftwind()
# s.magic_transform("enhanced")
# s.talk()
# print(s.get_alter_ego_owner())
# s.magic_transform("normal")



class ThirtyThirty(Horse):
    def __init__(self):
        self.__gun = False
        self.__walking_biped = False
        self._set_owner("Marshall Bravestarr")
        self._set_alter_ego(False)
        self._set_alter_ego_owner(False)
        self._set_battle_armour(False)
        self._set_talkability(True)
        self._set_colour("grey")
        self._set_transformability(True)
        self._set_wings(False)
        self._set_flyability(False)

    def __set_biped(self, value):
        self.__walking_biped = value

    def get_gun(self):
        return self.__gun

    def __set_gun(self, value):
        if value == "disarm":
            print("No gun")
            self.__gun = False
        elif value == "arm":
            print("Loading Sara Jane")
            self.__gun = True

    def magic_transform(self, status):
        super().magic_transform(status)
        if status == "enhanced":
            self.__set_biped(True)
            self.__set_gun("arm")
        else:
            self.__set_biped(False)
            self.__set_gun("disarm")

    def shoot_gun(self):
        if self.get_gun():
            print("snap")
        else:
            print("no gun, I'm not transformed")

# t = ThirtyThirty()
# # t.magic_transform("enhanced")
# t.shoot_gun()
# t.talk()

class Starlite(Horse): #no transform
    def __init__(self):
        self._set_character("egotistical")
        self.__rainbow = False
        self._set_owner("Rainbow Brite")
        self._set_alter_ego_owner(False)
        self._set_alter_ego(False)
        self._set_battle_armour(False)
        self._set_talkability(True)
        self._set_colour("white")
        self._set_flyability(False)
        self._set_wings(False)
        self._set_transformability(False)

    def get_rainbow(self):
        return self.__rainbow

    def set_rainbow(self, value):
        if value == "active":
            self.__rainbow = True
            print("here is the rainbow")
        elif value == "inactive":
            self.__rainbow = False
            print("no more rainbow")

    def ride_on_rainbow(self):
        if self.get_rainbow():
            print("Galopping on Rainbow Brite's Rainbow")
        else:
            print("I cannot fly without rainbow.")

    def talk(self):
        print("I'm the most magnificent horse in the universe")

# s = Starlite()
# s.magic_transform("enhanced")
# s.set_rainbow("active")
# s.ride_on_rainbow()
# s.set_rainbow("inactive")
# s.ride_on_rainbow()
# s.talk()

class CringerBattlecat(Cat):
    def __init__(self):
        self._set_alter_ego("BattleCat")
        self._set_transformability(True)
        self._set_owner("Adam")
        self._set_alter_ego_owner("He-man")
        self._set_talkability(True)
        self._set_colour("green with yellow stripes")
        self._set_battle_armour(False)
        self._set_character("coward and sleepy")

    def magic_transform(self, status):
        if status == "enhanced":
            self._set_battle_armour(True)
            self._set_character("brave and alert")
        else:
            self._set_battle_armour(False)
            self._set_character("coward and sleepy")

        super().magic_transform(status)


# cb = CringerBattlecat()
# cb.magic_transform("enhanced")
# cb.magic_transform("normal")
# cb.talk()


class Panthor(Cat):
    def __init__(self):
        self._set_owner("Skelletor")
        self._set_battle_armour(True)
        self._set_transformability(False)
        self._set_talkability(False)
        self._set_alter_ego(False)
        self._set_alter_ego_owner(False)
        self._set_colour("purple")


# p = Panthor()
# print(p.get_transformability())
# p.magic_transform("enhanced")
# p.talk()
