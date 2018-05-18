class Item(object):
    def __init__(self, name, description, amount):
        self.name = name
        self.description = description
        self.amount = int(amount)

class Character(object):
    def __init__(self, name, description, health, max_health, attack, defense, damage):
        self.name = name
        self.description = description
        self.health = health
        self.max_health = max_health
        self.attack = attack
        self.defense = defense
        self.damage = self.attack + damage

    def fight(self, enemy):
        while current_node.enemy.health != 0:
            print("You attack.")
            current_node.enemy.health = (player.damage - current_node.enemy.defense)
        if current_node.enemy.health == 0:
            print("The enemy is already dead, there is nothing else for you to fight.")
        if current_node.enemy is None:
            print("There are no enemies in this room.")

    def take_damage(self, enemy):
        while player.health != 0:
            print("The enemy attacks you.")
            player.health = (current_node.enemy.attack - player.defense)
            print("You lost " + current_node.enemy.attack + " health!")

    def grab(self):
        if current_node.item1 is not None:
            inventory.append(current_node.item1)
            current_node.item1 = None
        if current_node.item2 is not None:
            inventory.append(current_node.item2)
            current_node.item2 = None
        if current_node.item3 is not None:
            inventory.append(current_node.item3)
            current_node.item3 = None

    def stats(self):
        print("You have " + str(player.health) + " health out of " + str(player.max_health) + ".")
        print("Your attack is " + str(player.attack) + " and your weapon has " + str(player.damage) + " you total is" +
              str(player.damage + player.attack) + ".")
        print("Your defense is " + str(player.defense) + ".")

    def unlock(self):
        print("In the box is a key. This isn;t a regular key, and it is accompanied with a note.")
        print("The note reads 'This key now belongs to you, the only one whom could defeat the forest spider, Gohma,"
              "and successfully open the box. Now take the key, and save the forests!'")

    def interact(self, enemy):
        print("The enemy's name is " + current_node.enemy.name + ".")
        print(current_node.enemy.description)
        print("The enemy has " + current_node.enemy.health + " health.")
        print("The enemy has " + current_node.enemy.attack + " attack.")
        print("The enemy has " + current_node.enemy.defense + " defense")

    def equip(self):
        equip = input("What do you want to equip? ")
        if equip in inventory:
            self.attack = self.attack + self.damage


class Enemy(Character):
    def __init__(self, name, description, health, max_health, attack, defense, damage):
        super(Enemy, self).__init__(name, description, health, max_health, attack, defense, damage)


class Room(object):
    def __init__(self, name, north, south, east, west, up, down, description, item1, item2, item3, enemy):
        self.name = name
        self.north = north
        self.south = south
        self.east = east
        self.west = west
        self.up = up
        self.down = down
        self.lock1 = True
        self.lock2 = True
        self.lock3 = True
        self.lock4 = True
        self.description = description
        self.item1 = item1
        self.item2 = item2
        self.item3 = item3
        self.enemy = enemy

    def move(self, direction):
        global current_node
        current_node = globals()[getattr(self, direction)]

# Items


class Weapon(Item):
    def __init__(self, name, description, damage, ability, attack_type):
        super(Weapon, self).__init__(name, description, 0)
        self.damage = damage
        self.ability = ability
        self.attack_type = attack_type


class Sword(Weapon):
    def __init__(self, name, description, damage, ability, melee):
        super(Sword, self).__init__(name, description, damage, ability, melee)
        self.attack_type = melee

    def attack(self, enemy):
        print("You attack.")
        enemy.health = enemy.health - self.damage


class Bow(Weapon):
    def __init__(self, name, description, damage, ability, ranged):
        super(Bow, self).__init__(name, description, damage, ability, ranged)
        self.attack_type = ranged

    def attack(self, enemy):
        print("You shoot the enemy.")
        enemy.health = enemy.health - self.damage


class Gauntlet(Weapon):
    def __init__(self, name, description, damage, ability, melee):
        super(Gauntlet, self).__init__(name, description, damage, ability, melee)

    def attack(self, enemy):
        print("You attack.")
        enemy.health = enemy.health - self.damage


class Bomb(Weapon):
    def __init__(self, name, description, damage, ability, ranged):
        super(Bomb, self).__init__(name, description, damage, ability, ranged)

    def attack(self, enemy):
        print("You throw a bomb at the enemy.")
        enemy.health = enemy.health - self.damage


class Consumable(Item):
    def __init__(self, name, description, amount):
        super(Consumable, self).__init__(name, description, 0)
        self.use = False
        self.amount = int(amount)

    def obtain(self):
        self.amount = self.amount + 1
        print("You have obtained a %s" % self.name)


class HpPotion(Consumable):
    def __init__(self):
        super(HpPotion, self).__init__("Healing Potion", "A potion the will restore 3 HP.", 0)

    def use(self):
        self.use = True
        player.health = player.health + 3
        player.max_health = player.max_health
        self.amount = self.amount - 1
        print("You have used a health potion.")
        if player.player_health > player.max_health:
            player.player_health = player.max_health


class HeartContainer(Consumable):
    def __init__(self):
        super(HeartContainer, self).__init__("Heart Container",
                                             "A heart container, which permanently increases your maximum health.", 0)

    def use(self):
        self.use = True
        player.max_health = player.max_health + 5
        self.amount = self.amount - 1
        print("Your health has been upgraded by 5 points!")


class AtkPotion(Consumable):
    def __init__(self):
        super(AtkPotion, self).__init__("Attack Potion", "A potion that permanently increases your attack by one.", 0)

    def use(self):
        self.use = True
        player.attack = player.attack + 1
        print("Your attack has been permanently upgraded by 1!")


class DefPotion(Consumable):
    def __init__(self):
        super(DefPotion, self).__init__("Defense Potion",
                                        "A potion that permanently decreases the damage you receive by one.", 0)

    def use(self):
        self.use = True
        player.defense = player.defense + 1
        print("Your defense has been permanently upgraded by 1!")


class KeyItem(Item):
    def __init__(self, name, description):
        super(KeyItem, self).__init__(name, description, 0)


class Key(KeyItem):
    def __init__(self):
        super(Key, self).__init__("Key", "A key, it may be used for something, but it's a little rusty.")


class Torch(KeyItem):
    def __init__(self):
        super(Torch, self).__init__("Torch", "A very warm torch, and may be of some use in colder weather.")


class GohmaEye(KeyItem):
    def __init__(self):
        super(GohmaEye, self).__init__("Gohma's Eye",
                                       "The eye of the Forest Spider, Gohma, and may hold some hidden treasures.")


class TreeTreasure(KeyItem):
    def __init__(self):
        super(TreeTreasure, self).__init__("The Great Tree's Amulet",
                                           "The amulet of The Great Tree, and is said to be the creator of the "
                                           "forests. Intense aura emits from the bottom of the amulet.")


health_potion = HpPotion()
atk_potion = AtkPotion()
def_potion = DefPotion()
heart_container = HeartContainer()
key0 = Key()
eye = GohmaEye()
torch0 = Torch()
treasures = TreeTreasure()
player = Character("You", "It's you, what else do you need to know?", 10, 10, 0, 0, 0)
ogre1 = Enemy("Ogre", "A big, bad ogre, that is hostile to nearly everything.", 10, 10, 3, 3, 3)
goblin = Enemy("Goblin", "A small goblin, with no common sense.", 5, 5, 1, 0, 1)
sapling = Enemy("Sapling", "A small corrupt sapling. It has sharp vines that are dangerous.", 8, 8, 5, 1, 5)
fire = Enemy("Fire Elemental", "A small, young fire elemental, that hasn't grown enough to be strong. It has small "
                               "embers that fly towards its foes.", 5, 5, 3, 5, 5)
ghoul = Enemy("Ghoul", "A disgusting ghoul, that isn't afraid to attack.", 12, 12, 5, 0, 5)
ice = Enemy("Ice Elemental", "An ice elemental, and the guardian of the gauntlet. It uses freezing temperatures to "
                             "attack its foes.", 15, 15, 6, 3, 6)
troll = Enemy("Forest Troll", "A forest troll is a troll that lives in the forest. They are usually hostile and "
                              "ruthless, especially to human-like beings.", 15, 15, 7, 4, 7)
boss = Enemy("Gohma", "The guardian of the Tree's Treasure, and the only thing that stand in your way now.",
             30, 30, 10, 5, 10)
sword = Sword("Iron sword", "A durable, iron sword.", 3, None, None)
gt_sword = Sword("Great Tree Sword", "The weapon of the Great Tree.", 10, TreeTreasure, None)
bow = Bow("Arcane Bow", "A bow. It's doesn't require arrows, and can shoot without them.", 4, None, None)
gauntlet = Gauntlet("Powerless Gauntlet", "A gauntlet that holds no power.", 2, None, None)
f_gauntlet = Gauntlet("Fire Gauntlet", "The gauntlet, infused with the element of fire.", 8, Torch, None)
bomb = Bomb("Ivy Bomb", "A bomb, infused with the essence of nature. It regrows easily, which means it will come "
                        "back after using it.", 8, None, None)
# Initialize Rooms
tree_house = Room("Tree House", None, None, None, None, None, "village",
                  "You have lived in this house your entire life. You still have your locked box that is stuck to the "
                  "wall. It seems to have a socket for a ball. You can climb down to the village.",
                  health_potion, heart_container, None, None)
village = Room("Village", "north_village", "south_village", None, "shop", "tree_house", None,
               "The village is deserted now, and you area the only one left. The old man's shop lies to the west, and "
               "there is a clearing to the north. The exit to the village is south.",
               None, None, None, None)
shop = Room("Old Man's Shop", "north_village", None, "village", None, None, None,
            "An old wooden plank is on the ground, and it seems to serve no use, but it may come in handy. There are "
            "two exits to the north and the west.", atk_potion, def_potion, health_potion, None,)
north_village = Room("North of Village", None, "village", None, "shop", None, None,
                     "The north of the village. It's nice and clear, but not much else.", None, None, None, None,)
south_village = Room("South of Village", "village", "lost_forest", None, None, None, None,
                     "The south of the village. There is a small hole to the south, and the locked gate to the west.",
                     None, None, None, None)
lost_forest = Room("Lost Forest", "south_village", "treasure", None, "winding", None, None,
                   "The sacred ground of the forest people. There is a small crack that you could go through with "
                   "sparks flying out of it, and a narrow path leads to the west.", heart_container, None, None, None,)
treasure = Room("Treasure Room", "lost_forest", None, None, None, None, None,
                "A treasure chest is slightly open, and is glowing. The only exit is where you came from.", sword,
                heart_container, None, None)
winding = Room("Winding Road", None, None, "lost_forest", "forest", None, None,
               "A man seems to be sleeping, not even the loudest noise could wake him up. The path west leads to the"
               " forest.", None, None, None, None)
forest = Room("Forest", "dark_cave", None, "winding", "fort", None, None,
              "The forest of the non-forest people. There lies a cave to the north, and a suspicious looking fort to "
              "the west. ", def_potion, None, None, None)
fort = Room("Goblin Fort", None, None, "forest", "storage", None, None,
            "A small goblin with a stick charges towards you! A large door to the west leads to the storage room.",
            heart_container, None, None, goblin)
storage = Room("Storage", "torch", None, "fort", None, None, None,
               "A simple storage room, may be good for hiding stuff. There is an open door to the north with a bright "
               "light coming through it.", None, None, None, None)
torch = Room("Mystic", None, "storage", None, None, None, None,
             "A magical torch is held in the center of the room, and it seems to be up for grabs! The only exit is "
             "where you came from.", torch0, Bow, heart_container, fire)
dark_cave = Room("Dark Cave", None, "forest", "ogre", "gt_entrance", None, None,
                 "You cannot see anything, and should use a light source to light up the room. There are exits "
                 "to the east and west.", None, None, None, None)
ogre = Room("Ogre Cave", "cave", None, None, "dark_cave", None, None,
            "An ogre sleeps in the middle of the room, it'd be best not to wake it. The path leads to the "
            "north", None, None, None, ogre1)
cave = Room("Cave", None, "ogre", None, "icy_forest", None, None,
            "A dead body rots on the floor, and you feel a chill go down your spine. You get colder from "
            "the exit to the west.", None, None, None, None)
icy_forest = Room("Icy Forest", "frozen_keep", None, "cave", None, None, None,
                  "It's very cold, and frozen bodies lie on the floor. The source of the ice is probably from the "
                  "fortress to the north, which is said to hold a very powerful weapon.", None, None, None, ghoul)
frozen_keep = Room("Frozen Fortress", None, "icy_forest", None, None, None, None,
                   "It's extremely cold, and there is a frozen gauntlet on a pedestal. You may be able to melt it "
                   "with some fire. The only exit is where you came from.", Gauntlet, atk_potion, def_potion,
                   ice)
gt_entrance = Room("Great Tree Entrance", None, None, "dark_cave", "gt_level_one", None, None,
                   "In front of you lies the Great Tree, the god of the forest people. The gate of the great "
                   "tree is open for you to claim the treasure for the fallen forest people.", None, None, None,
                   troll)
gt_level_one = Room("Great Tree (Floor One)", None, None, None, None, "gt_level_two", "torch",
                    "The first floor of the the Great Tree. There is a hole in the ground, and a vine ladder leading "
                    "to the next level", heart_container, health_potion, None, troll)
gt_level_two = Room("Great Tree (Floor Two)", None, None, None, None, "gt_level_three", "gt_level_one",
                    "The second floor of the Great Tree. A vine ladder continues higher up the tree, to the third "
                    "floor.", atk_potion, def_potion, None, None)
gt_level_three = Room("Great Tree (Floor Three)", None, None, None, None, "lair", "gt_level_two",
                      "The third floor of the Great Tree. A vine ladder continues even higher, to the fourth floor. "
                      "A sign reads, 'BEWARE OF MONSTERS!!!'", None, None, None, troll)
lair = Room("Gohma's Lair", "great_tree_treasures", None, None, None, "tree_house", "gt_level_three",
            "The last thing that stands between you and the forest treasure is the forest spider, 'Gohma'. "
            "Retrieve it's eye, and you may be able to open the lock, and get to the treasure. The treasure "
            "room is locked with a keyhole to the north. A mysterious hole is above you, and a ladder drops from "
            "the hole, enter, at your own risk.", heart_container, None, None, boss)
great_tree_treasures = Room("Great Tree Treasure Room", None, "lair", None, None, None, None,
                            "In front of you lies the Great Tree's Treasure, the Amulet of the Forest Spirit. It is "
                            "now yours to keep, but beware, it may bring an evil curse with it...", TreeTreasure,
                            atk_potion, def_potion, None)

directions = ['north', 'south', 'east', 'west', 'up', 'down']
short_directions = ['n', 's', 'e', 'w', 'u', 'd']
offense = ['attack', 'fight']
defence = ['dodge', 'roll', 'move']
obtain = ['take', 'pick up']
key = ['open', 'use']
items = ['use potion', 'use item', 'use', 'items']
status = ['inventory', 'status', 'stats']
inventory = []
current_node = tree_house
empty = True
move = True
player_hp = 10
weapon = None

while True:
    print(current_node.name)
    print(current_node.description)
    command = input('>_').lower()
    for health_potion in inventory:
        health_potion.amount = health_potion.amount + 1
    for atk_potion in inventory:
        atk_potion.amount = atk_potion.amount + 1
    for def_potion in inventory:
        def_potion.amount = def_potion.amount + 1
    for heart_container in inventory:
        heart_container.amount = heart_container.amount + 1

    if current_node.enemy is True:
        print("There is an enemy in your area!")
        print("You can't escape until the enemy been defeated!")

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

    elif command in offense:
        player.fight(current_node.enemy)
        player.take_damage(player)

    elif command in defence:
        player.health = player.health + current_node.enemy.attack

    elif command in ["health potion", "heal"]:
        if health_potion.amount == 0:
            print("You don't have any health potions.")
        elif player.health == player.max_health:
            print("You already have full health.")
        else:
            player.health = player.health + 5
            player.max_health = player.max_health
            health_potion.amount = health_potion.amount - 1
            print("You have used a health potion.")
            if health_potion.amount == 0:
                print("You ran out of health potions.")
        for health_potion in inventory:
            health_potion.amount = health_potion.amount + 1

    elif command == "attack potion":
        if atk_potion.amount == 0:
            print("You don't have any attack potions.")
        else:
            player.attack = player.attack + 3
            atk_potion.amount = atk_potion.amount - 1
            print("You have used an attack potion.")
            if atk_potion.amount == 0:
                print("You ran out of attack potions.")
        for atk_potion in inventory:
            atk_potion.amount = atk_potion.amount + 1

    elif command == "defense potion":
        if def_potion.amount == 0:
            print("You don't have any defense potions.")
        else:
            player.defense = player.defense + 3
            def_potion.amount = def_potion.amount - 1
            print("You have used a defense potion.")
            if def_potion.amount == 0:
                print("You ran out of defense potions.")
        for def_potion in inventory:
            def_potion.amount = def_potion.amount + 1

    elif command == "heart container":
        if heart_container.amount == 0:
            print("You don't have any heart containers.")
        else:
            player.max_health = player.max_health + 5
            player.health = player.max_health
            heart_container.amount = heart_container.amount - 1
            print("You have used a heart container.")
            if heart_container.amount == 0:
                print("You ran out of heart containers.")

    elif command in ["sword", "iron sword"]:
        weapon = sword
        player.damage = player.damage + sword.damage
        print("You have the 'Sword' equipped.")

    elif command == "great tree sword":
        weapon = gt_sword
        player.damage = player.damage + sword.damage
        print("You have the 'Great Tree Sword' equipped.")

    elif command in ["bow", "magic bow"]:
        weapon = bow
        player.damage = player.damage + bow.damage
        print("You have the 'Magic Bow' equipped.")

    elif command in ["bomb", "ivy bomb"]:
        weapon = bomb
        player.damage = player.damage + bomb.damage
        print("You have the 'Ivy Bomb' equipped.")

    elif command in ["inventory", 'i']:
        if empty is True:
            print("You have nothing in your inventory.")
        else:
            for Item in inventory:
                print(Item.name)

    elif command in ["pick up", "p"]:
        player.grab()
        empty = False

    elif command in ["stats", "ss"]:
        player.stats()

    elif command in ["help", "h"]:
        print("You can move with 'north', 'south,' 'east,' 'west,' 'up,' or 'down' or the first letter of each "
              "direction.")
        print("You can pick up items, if there are any, by typing 'pick up' or 'p'.")
        print("You can use items by typing their name.")
        print("You can attack or defend by typing 'attack' or 'defend' or 'a' or 'df'.")
        print("You can equip a weapon by typing the name of the weapon.")
        print("You can check the enemy by typing 'enemy'.")
        print("You can check your inventory by typing 'inventory' or 'i'.")
        print("You can check your stats by typing 'stats'. or 'ss'")
        print("You can check what weapon you have equipped by typing 'weapon'.")

    elif command == weapon:
        if weapon is None:
            print("You don't have any weapon equipped.")
        else:
            print(weapon.name)

    elif command == "enemy":
        player.interact(current_node.enemy)

    elif command in key:
        if key0 in inventory:
                current_node.lock1 = False
                print("You have unlocked the door.")
        if torch0 in inventory:
                current_node.lock2 = False
                print("The ice on the door melts.")
        if eye in inventory:
                current_node.lock3 = False
                print("You have unlocked the box.")
        if TreeTreasure in inventory:
                current_node.lock4 = False
                print("You have unlocked the door.")

    elif current_node.lock1 is True:
        if current_node == great_tree_treasures:
            current_node = lair
            print("You can't go that way without the Key.")

    elif current_node.lock2 is True:
        if current_node == frozen_keep:
            current_node = icy_forest
            print("You can't go that way without the Torch.")

    elif current_node.lock3 is False:
        player.unlock()

    elif current_node.enemy is not None:
        if current_node.enemy.health == 0:
            move = True
        elif current_node.enemy.health > 0:
            move = False

    elif boss.health == 0:
        print("You have defeated the Forest Spider, Gohma, and have now acquired it's eye, which is rumored to unlock "
              "the secrets of the Great Tree.")
        print("Pick up the eye from Gohma.")
        eye = lair.item3

    elif player.health > player.max_health:
        player.health = player.max_health

    elif player.health == 0:
        print("You have died..."
              "GAME OVER")
        quit()

    elif current_node == great_tree_treasures:
        print("You've made it! The treasure is now yours, but beware, it wasn't well protected for no reason...")
        quit(0)

    elif command == "up up down down left right left right b a start":
        print("Why are you trying to use cheat codes?")
        print("GAME OVER")
        quit()

    else:
        print("Command not recognized.")

    print("___________________________________________________________________________________________________________"
          "___________________________________________________________________________________________________________")
