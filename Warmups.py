# New python file: Warmups.py

# 12.4.17

# Write a Python program
# which accepts the user's
# first and last name
# and print them in reverse order
# with a space in between


def reverse_order(first_name, last_name):
    print("%s, %s" % (last_name, first_name))  # Concatenation


def reverse_order1():
    first_name = input("First Name")
    last_name = input("Last Name")
    print("%s, %s" % (last_name, first_name))

# 12.5.17


def add_py(name):
    print("%s.py" % name)

# 12.6.17


def add(one, two, three):
    print(one + two + three)


add(1, 2, 3)


# 12.7.17


def repeat(string):
    print(string)
    print(string)
    print(string)

    for x in range(3):
        print(string)
