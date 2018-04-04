# class Vehicle(object):
#     def __init__(self, seats, engine_type, turning_mechanism):
#         self.seats = seats
#         self.engine_type = engine_type
#         self.turning_mechanism = turning_mechanism
#
#     def move(self):
#         print("You move forward")
#
#     def change_direction(self):
#         print("You change direction")
#
#
# class Car(Vehicle):
#     def __init__(self, seats, horsepower):
#         super(Car, self).__init__(seats, 'engine', 'steering wheel')
#         self.hp = horsepower
#
#     def turn_on(self):
#         print("You turn the key and the engine starts")
#
#
# test_car = Car(4, 9001)
# test_car.turn_on()
# test_car.change_direction()
# print(test_car.turning_mechanism)
#
#
# class KeylessCar(Car):
#     def __init__(self, seats, hp):
#         super(KeylessCar, self).__init__(seats, hp)
#
#     def turn_on(self):
#         print("You push the button and the car turns on")
#
#
# test_car.turn_on()
# cool_car = KeylessCar(4, 9002)
# cool_car.turn_on()
#
#
# class Tesla(Car):
#     def __init__(self, seats):
#         super(Tesla, self).__init__(seats, 500)
#
#     def launch(self):
#         print("You launch the car into low earth orbit.")
inventory = [ ]

class Item(object):
    def __init__(self, name, description):
        self.name = name
        self.description = description


class Weapon(Item):
    def __init__(self, name, description, damage, ability, attack_type):
        super(Weapon, self).__init__(name, description)
        self.damage = damage
        self.ability = ability
        self.attack_type = attack_type


class Sword(Weapon):
    def __init__(self, name, description, damage, ability, melee):
        super(Sword, self).__init__(name, description, damage, ability, melee)
        self.attack_type = melee

    def equip(self):
        self.damage = self.damage + self.attack

    def attack(self):
        print("You attack.")
        self.health = self.health - self.damage

class Bow(Weapon):
    def __init__(self, name, description, damage, ability, ranged):
        super(Bow, self).__init__(name, description, damage, ability, ranged)
        self.attack_type = ranged

    def equip(self):
        self.damage = self.damage + self.attack

    def attack(self):
        print("You attack.")
        self.health = self.health - self.damage

class Gauntlet(Weapon):
    def __init__(self, name, description, damage, ability, melee):
        super(Gauntlet, self).__init__(name, description, damage, ability, melee)

    def equip(self):
        self.damage = self.damage + self.attack

    def attack(self):
        print("You attack.")
        self.health = self.health - self.damage

class Bomb(Weapon):
    def __init__(self, name, description, damage, ability, ranged):
        super(Bomb, self).__init__(name, description, damage, ability, ranged)

    def equip(self):
        self.damage = self.damage + self.attack

    def attack(self):
        print("You attack.")
        self.health = self.health - self.damage

class Consumable(Item):
    def __init__(self, name, description):
        super(Consumable, self).__init__(name, description)
        self.use = False
        self.amount = 0

    def obtain(self):
        self.amount = self.amount + 1
        print("You have obtained a %s" % self.name)


class HP_Potion(Consumable):
    def __init__(self):
        super(HP_Potion, self).__init__("Healing Potion", "A potion the will restore 3 HP.")

    def use(self):
        self.use = True
        self.health = self.health + 3
        self.amount = self.amount - 1
        print("You have used a health potion.")


class Heart_Container(Consumable):
    def __init__(self):
        super(Heart_Container, self).__init__("Heart Container",
                                              "A heart container, which permanently increases your maximum health.")

    def use(self):
        self.use = True
        self.health = self.health + 5
        self.amount = self.amount - 1
        print("Your health has been upgraded by 5 points!")


class Atk_Potion(Consumable):
    def __init__(self):
        super(Atk_Potion, self).__init__("Attack Potion", "A potion that permanently increases your attack by one.")

    def use(self):
        self.use = True
        self.attack = self.attack + 1
        print("Your attack has been permanently upgraded by 1!")


class Def_Potion(Consumable):
    def __init__(self):
        super(Def_Potion, self).__init__("Defense Potion",
                                         "A potion that permanently decreases the damage you receive by one.")

    def use(self):
        self.use = True
        self.defense = self.defense + 1
        print("Your defense has been permanently upgraded by 1!")


class Key_Item(Item):
    def __init__(self, name, description):
        super(Key_Item, self).__init__(name, description)


class Key(Key_Item):
    def __init__(self):
        super(Key, self).__init__("Key", "A key, it may be used for something, but it's a little rusty.")

    def unlock(self):
        self.lock = False
        print("You have unlocked the door.")


class Torch(Key_Item):
    def __init__(self):
        super(Torch, self).__init__("Torch", "A very warm torch, and may be of some use in colder weather.")

    def unlock(self):
        if Torch in inventory:
            self.lock = False
            print("The ice on the door melts")


class Gohma_Eye(Key_Item):
    def __init__(self):
        super(Gohma_Eye, self).__init__("Gohma's Eye",
                                        "The eye of the Forest Spider, Gohma, and may hold some hidden treasures.")

    def unlock(self):
        if Gohma_Eye in inventory:
            self.lock = False
            print("You have unlocked the door.")


class Tree_Treasure(Key_Item):
    def __init__(self):
        super(Tree_Treasure, self).__init__("The Great Tree's Amulet",
                                            "The amulet of The Great Tree, and is said to be the creator of the "
                                            "forests. Intense aura emits from the bottom of the amulet.")

    def unlock(self):
        if Tree_Treasure in inventory:
            self.lock = False
            print("You have unlocked the door.")


