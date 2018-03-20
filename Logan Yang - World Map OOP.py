class Room(object):
    def __init__(self, name, north, south, east, west, up, down, description):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.lock = True
        self.description = description

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]


class Character(object):
    def __init__(self, name, description, health, move, attack, defense):
        self.name = name
        self.alive = True
        self.description = description
        self.attack = False
        self.take_damage = False
        self.health = health
        self.movement = move
        self.attack = attack
        self.defense = defense

    def interact(self):
        print(self.name)
        print(self.description)
        print(self.health)

    def hit(self):
        self.take_damage = True
        self.health = self.health - 1
        print("You hit the enemy.")
        print(self.health)
        if self.health == 0:
            print("The enemy dies.")
            self.alive = False
        elif self.health < 0:
            print("Your enemy is dead.")
        self.take_damage = False

    def take_hit(self):
        self.take_damage = True
        self.health = self.health - 1
        print("You take damage.")
        if self.health == 0:
            print("You have died. GAME OVER.")
            quit()

    def move(self):
        self.movement = True
        print("The enemy moves!")
        self.movement = False

    def status(self):
        print("%s/5 health left" % self.health)


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


class Bow(Weapon):
    def __init__(self, name, description, damage, ability, ranged):
        super(Bow, self).__init__(name, description, damage, ability, ranged)
        self.attack_type = ranged


class Gauntlet(Weapon):
    def __init__(self, name, description, damage, ability, melee):
        super(Gauntlet, self).__init__(name, description, damage, ability, melee)


class Bomb(Weapon):
    def __init__(self, name, description, damage, ability, ranged):
        super(Bomb, self).__init__(name, description, damage, ability, ranged)


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
        self.use = False


class Heart_Container(Consumable):
    def __init__(self):
        super(Heart_Container, self).__init__("Heart Container", 
                                              "A heart container, which permanently increases your maximum health.")

    def use(self):
        self.use = True
        self.health = self.health + 5
        self.amount = self.amount - 1
        print("Your health has been upgraded by 5 points!")
        self.use = False


class Atk_Potion(Consumable):
    def __init__(self):
        super(Atk_Potion, self).__init__("Attack Potion", "A potion that permanently increases your attack by one.")

    def use(self):
        self.use = True
        self.attack = self.attack + 1
        print("Your attack has been permanently upgraded by 1!")
        self.use = False


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


class Gohma_Eye(Key_Item):
    def __init__(self):
        super(Gohma_Eye, self).__init__("Gohma's Eye",
                                        "The eye of the Forest Spider, Gohma, and may hold some hidden treasures.")


class Tree_Treasure(Key_Item):
    def __init__(self):
        super(Tree_Treasure, self).__init__("The Great Tree's Amulet",
                                            "The amulet of The Great Tree, and is said to be the creator of the "
                                            "forests. Intense aura emits from the bottom of the amulet.")


# Initialize Rooms
tree_house = Room("Tree House", None, None, None, None, None, "village",
                  "You have lived in this house your entire life. You still have your locked box that is stuck to the "
                  "wall. It seems to have a socket for a ball. You can climb down to the village.")
village = Room("Village", "north_village", "south_village", "shop", None, "tree_house", None,
               "The village is deserted now, and you area the only one left. The old man's shop lies to the west, and "
               "there is a clearing to the north. The exit to the village is south.")
shop = Room("Old Man's Shop", "north_village", None, None, "village", None, None,
            "An old wooden plank is on the ground, and it seems to serve no use, but it may come in handy. There are "
            "two exits to the north and the west.")
north_village = Room("North of Village", None, "village", "shop", None, None, None,
                     "The north of the village. It's nice and clear, but not much else.")
south_village = Room("South of Village", "village", "lost_forest", None, None, None, None,
                     "The south of the village. There is a small hole to the south, and the locked gate to the west.")
lost_forest = Room("Lost Forest", "south_village", "treasure", None, "winding", None, None,
                   "The sacred ground of the forest people. There is a small crack that you could go through with "
                   "sparks flying out of it, and a narrow path leads to the west.")
treasure = Room("Treasure Room", "lost_forest", None, None, None, None, None,
                "A treasure chest is slightly open, and is glowing. The only exit is where you came from.",)
winding = Room("Winding Road", None, None, "lost_forest", "forest", None, None,
               "A man seems to be sleeping, not even the loudest noise could wake him up. The path west leads to the"
               " forest.")
forest = Room("Forest", "dark_cave", None, "winding", "fort", None, None,
              "The forest of the non-forest people. There lies a cave to the north, and a suspicious looking fort to "
              "the west. There is a durable sword on the ground.")
fort = Room("Goblin Fort", None, None, "forest", "storage", None, None,
            "A small goblin with a stick charges towards you! A large door to the west leads to the storage room.")
storage = Room("Storage", "torch", None, "fort", None, None, None,
               "A simple storage room, may be good for hiding stuff. There is an open door to the north with a bright "
               "light coming through it.")
torch = Room("Mystic", None, "storage", None, None, None, None,
             "A magical torch is held in the center of the room, and it seems to be up for grabs! The only exit is "
             "where you came from.")
dark_cave = Room("Dark Cave", None, "forest", "ogre", "gt_entrance", None, None,
                 "You cannot see anything, and should use a light source to light up the room. There are exits "
                 "to the east and west.")
ogre = Room("Ogre Cave", "cave", None, None, "dark_cave", None, None,
            "An ogre sleeps in the middle of the room, it'd be best not to wake it. The path leads to the "
            "north")
cave = Room("Cave", None, "ogre", None, "icy_forest", None, None,
            "A dead body rots on the floor, and you feel a chill go down your spine. You get colder from "
            "the exit to the west.")
icy_forest = Room("Icy Forest", "frozen_keep", None, "cave", None, None, None,
                  "It's very cold, and frozen bodies lie on the floor. The source of the ice is probably from the keep "
                  "to the north, which is said to hold a very powerful weapon.")
frozen_keep = Room("Frozen Keep", None, "icy_forest", None, None, None, None,
                   "It's extremely cold, and there is a frozen gauntlet on a pedestal. You may be able to melt it "
                   "with some fire. The only exit is where you came from.")
gt_entrance = Room("Great Tree Entrance", None, None, "dark_cave", "gt_level_one", None, None,
                   "In front of you lies the Great Tree, the god of the forest people. The gate of the great "
                   "tree is open for you to claim the treasure for the fallen forest people.")
gt_level_one = Room("Great Tree (Floor One)", None, None, None, None, "gt_level_two", "torch",
                    "The first level of the the Great Tree. There is a hole in the ground, and a vine ladder leading "
                    "to the next level")
gt_level_two = Room("Great Tree (Level Two)", None, None, None, None, "gt_level_three", "gt_level_one",
                    "The second level of the Great Tree. A vine ladder continues even higher, to the third floor.")
gt_level_three = Room("Great Tree (Level Three)", None, None, None, None, "lair", "gt_level_two",
                      "The third level of the Great Tree. A vine ladder continues even higher, to the fourth floor. "
                      "A sign reads, 'BEWARE OF MONSTERS!!!'")
lair = Room("Gohma's Lair", "great_tree_treasures", None, None, None, "tree_house", "gt_level_three",
            "The last thing that stands between you and the forest treasure is the forest spider, 'Gohma'. "
            "Retrieve it's eye, and you may be able to open the lock, and get to the treasure. The treasure "
            "room is locked with a keyhole to the north. A mysterious hole is above you, and a ladder drops from "
            "the hole, enter, at your own risk.")
great_tree_treasures = Room("Great Tree Treasures", None, "lair", None, None, None, None,
                            "In front of you lies the Great Tree's Treasure, the Amulet of the Forest Spirit. It is "
                            "now yours to keep, but beware, it may bring an evil curse with it...")

directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']
current_node = tree_house

while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_').lower()
    if command == 'quit':
        quit(0)
    elif command in short_directions:
        # Look for which command we typed in
        pos = short_directions.index(command)
        # Change the command to be the long term
        command = directions[pos]
    if command in directions:
        try:
            current_node.move(command)
        except KeyError:
            print("You can't go that way.")
    else:
        print("Command not recognized.")
