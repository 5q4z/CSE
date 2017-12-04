# New python file: Warmups.py

# 12.4.17
# Write a Python program
# which accepts the user's
# first and last name
# and print them in reverse order
# with a space in between


def reverse_order(first_name, last_name):
    print("%s, %s" % (last_name, first_name)) # Concatenation


def reverse_order():
    first_name = input("First Name")
    last_name = input("Last Name")
    print("%s, %s" % (last_name, first_name))