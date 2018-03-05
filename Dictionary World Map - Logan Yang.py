world_map = {
    'TREEHOUSE': {
        'NAME': "Tree house",
        'DESCRIPTION': "You've lived in this house your entire life. You still have your locked box that is stuck to "
                       "the wall. It seems to have a socket for a ball. You can climb down to the village.",
        'PATHS': {
            'DOWN': 'VILLAGE'
        }
    },
    'VILLAGE': {
        'NAME': "Village",
        'DESCRIPTION': "The village is deserted now, and you area the only one left. The old man's shop lies to the "
                       "west, and there is a clearing to the north. The exit to the village is south.",
        'PATHS': {
            'NORTH': 'NORTHVILLAGE',
            'WEST': 'SHOP',
            'SOUTH': 'SOUTHVILLAGE',
            'UP': 'TREEHOUSE'
        }
    },
    'SHOP': {
        'NAME': "Old Man's Shop",
        'DESCRIPTION': "An old wooden plank is on the ground, and it seems to serve no use, but may come in handy. "
                       "There are two exits to the north and the south.",
        'PATHS': {
            'NORTH': 'NORTHVILLAGE',
            'EAST': 'VILLAGE'
        }
    },
    'NORTHVILLAGE': {
        'NAME': "North of Village",
        'DESCRIPTION': "The north of the village. It's nice and clear, but not much else.",
        'PATHS': {
            'EAST': 'SHOP',
            'SOUTH': 'VILLAGE'
        }
    },
    'SOUTHVILLAGE': {
        'NAME': "South of Village",
        'DESCRIPTION': "The south of the village. There is a small hole to the south, and the locked gate to the west.",
        'PATHS': {
            'NORTH': 'VILLAGE',
            'SOUTH': 'LOSTFOREST'
        }
    },
    'LOSTFOREST': {
        'NAME': "The Lost Forest",
        'DESCRIPTION': "The sacred ground of the forest people. There is a small crack that you could go through with "
                       "sparks flying out of it, and a narrow path leads to the west.",
        'PATHS': {
            'NORTH': 'SOUTHVILLAGE',
            'SOUTH': 'SMALL',
            'WEST': 'PATH'
        }
    },
    'SMALL': {
        'NAME': "Small Room",
        'DESCRIPTION': "A treasure chest is slightly open, and is glowing. The only exit is where you came from.",
        'PATHS': {
            'NORTH': "LOSTFOREST"
        }
    },
    'PATH': {
        'NAME': "Narrow Path",
        'DESCRIPTION': "A man seems to be sleeping, not even the loudest noise could wake him up. The path west leads"
                       " to the forest.",
        'PATHS': {
            'EAST': "LOSTFOREST",
            'WEST': "FOREST"
        }
    },
    'FOREST': {
        'NAME': "Forest",
        'DESCRIPTION': "The forest of the non-forest people. There lies a cave to the north, and a suspicious looking"
                       " fort to the west. There is a durable sword on the ground.",
        'PATHS': {
            'EAST': "PATH",
            'NORTH': "DARK",
            'WEST': "FORT"
        }
    },
    'FORT': {
        'NAME': "Goblin Fort",
        'DESCRIPTION': "A small goblin with a stick charges towards you! A large door is to the west.",
        'PATHS': {
            'EAST': "FOREST",
            'WEST': "STORAGE"
        }
    },
    'STORAGE': {
        'NAME': "Storage Room",
        'DESCRIPTION': "A simple storage room, may be good for hiding stuff. There is an open door to the north with a "
                       "bright light coming through it.",
        'PATHS': {
            'NORTH': "TORCH",
            'EAST': "FORT"
        }
    },
    'TORCH': {
        'NAME': "Torch Room",
        'DESCRIPTION': "A magical torch is held in the center of the room, and it seems to be up for grabs! The only"
                       "exit is where you came from.",
        'PATHS': {
            'SOUTH': "STORAGE"
        }
    },
    'DARK': {
        'NAME': "Dark Cave",
        'DESCRIPTION': "You cannot see anything, and should use a light source to light up the room. There are exits "
                       "to the east and west ",
        'PATHS': {
            'WEST': 'ENTRANCE',
            'EAST': 'OGRE'
        }
    },
    'OGRE': {
        'NAME': "Ogre home",
        'DESCRIPTION': "An ogre sleeps in the middle of the room, it'd be best not to wake it. The path leads to the"
                       " north",
        'PATHS': {
            'WEST': 'DARK',
            'NORTH': 'CAVE'
        }
    },
    'CAVE': {
        'NAME': "Cave",
        'DESCRIPTION': "A dead body rots on the floor, and you feel a chill go down your spine. You get colder from "
                       "the entrance to the west.",
        'PATHS': {
            'WEST': 'COOL',
            'SOUTH': 'OGRE'
        }
    },
    'COOL': {
        'NAME': "Cool Cave",
        'DESCRIPTION': "It's very cold, and frozen bodies lie on the floor. It's getting even colder to the "
                       "north.",
        'PATHS': {
            'NORTH': 'FROZEN',
            'EAST': 'CAVE'
        }
    },
    'FROZEN': {
        'NAME': "Frozen Cave",
        'DESCRIPTION': "It's extremely cold, and there is a frozen gauntlet on a pedestal. You may be able to melt it "
                       "with some fire. The only exit is where you came from.",
        'PATHS': {
            'SOUTH': 'COOL'
        }
    },
    'ENTRANCE': {
        'NAME': "Great Tree Entrance",
        'DESCRIPTION': "In front of you lies the Great Tree, the god of the forest people. The gate inside the great "
                       "tree is open for you to claim the treasure for the forest people.",
        'PATHS': {
            'WEST': 'TREEONE',
            'EAST': 'DARK'
        }
    },
    'TREEONE': {
        'NAME': "Great Tree (Floor One)",
        'DESCRIPTION': "The first level of the the Great Tree. There is a hole in the ground, and a vine ladder leading"
                       " to the next level",
        'PATHS': {
            'UP': 'TREETWO',
            'DOWN': 'TORCH'
        }
    },
    'TREETWO': {
        'NAME': "Great Tree (Floor Two)",
        'DESCRIPTION': "The second level of the Great Tree. A vine ladder continues even higher, to the third floor.",
        'PATHS': {
            'DOWN': 'TREEONE',
            'UP': 'BOSS'
        }
    },
    'TREETHREE': {
        'NAME': "Great Tree (Floor Three)",
        'DESCRIPTION': "The third level of the Great Tree. A vine ladder continues even higher, to the fourth floor. "
                       "A sign reads, 'BEWARE OF MONSTERS!!!'",
        'PATHS': {
            'DOWN': 'TREETWO',
            'UP': 'BOSS'
        }
    },
    'BOSS': {
        'NAME': "Gohma's Lair",
        'DESCRIPTION': "The last thing that stands between you and the forest treasure is the forest spider, Gohma. "
                       "Retrieve it's eye, and you may be able to open the lock, and get to the treasure. The treasure "
                       "room is locked with a keyhole to the north.",
        'PATHS': {
            'NORTH': 'TREASURE',
            'DOWN': 'TREETHREE'
        }
    },
    'TREASURE': {
        'NAME': "Great Tree Treasure Room",
        'DESCRIPTION': "In front of you lies the Great Tree's Treasure, the Amulet of the Forest Spirit. It is now "
                       "yours to keep, but beware, it may bring an evil curse with it...",
        'PATHS': {
            'SOUTH': 'BOSS'
        }
    },
}

current_node = world_map['TREEHOUSE']
directions = ['NORTH', 'SOUTH', 'EAST', 'WEST', 'UP', 'DOWN']

while True:
    print(current_node['NAME'])
    print(current_node['DESCRIPTION'])
    print(current_node['PATHS'])
    command = input('>_')
    if command == 'quit':
        quit(0)
    if command in directions:
        try:
            name_of_node = current_node['PATHS'][command]
            current_node = world_map[name_of_node]
        except KeyError:
            print("You cannot go that way.")
    else:
        print("Command not recognized.")
