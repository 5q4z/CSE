import string
'''
import random
print("Hello World")

# Logan Yang

print(3 + 5)
print(5 - 3)
print(3 * 5)
print(6 / 2)

print(3 ** 2)

# this makes a new line. In python 3.6, it looks like print()
print("See if you can figure this out")
print(13 % 12)

car_name = "Wiebe Mobile"
car_type = "Tesla"
car_cylinders = 8
car_mpg = 9000.1

# Inline printing
print("I have a car called the %s" % car_name)
print("I have a car called the %s. It's a %s" % (car_name, car_type))

# asking for input
name + input("What is your name? ")  # In python 3, it is just called input()
age + input("How old are you? ")
print("Wow, %s years old, that's REALLY old!" % age)

Functions


def print_hw():
    print("Hello World")


print_hw()
print_hw()
print_hw()


def say_hi(name):  # name is a parameter
    print("Hello %s." % name)
    print("Enjoy your day.")


say_hi("John")


def print_age(name, age):
    print("%s is %d years old." % (name, age))
    age += 1  # this is the same as age = age + 1
    print("Next year, they will be %d" % age)


print_age("John", 15)


def f(x):
    return x**3 + 4 * x**2 + 7 * x - 4


print(f(3))
print(f(4))
print(f(5))


# If statements


def grade_calc(percentage):
    if percentage >= 90:
        return "A"
    elif percentage >= 80:
        return "B"
    elif percentage >= 70:
        return "C"
    elif percentage >= 60:
        return "D"
    elif percentage < 60:
        return "F"


def happy_bday(name):
    print("Happy birthday to you" + ",")
    print("Happy birthday to you" + ",")
    print("Happy birthday dear %s," % name)
    print("Happy birthday to you" + ".")


happy_bday("John")


# Loops

for num in range(10):
    print(num + 1)


a = 1
while a < 10:
    print(a)
    a += 1


print(random.randint(0, 100))


print(1 == 1)
print(1 != 2)
print(10 <= 15)
print(not False)

# Recasting
c = '1'
print(c == 1)
print(int(c) == 1)  # Both are ints
print(c == str(1))  # Both are strings


# The input command ALWAYS gives a string
'''

# Lists
the_count = [1, 2, 3, 4, 5]
shopping_list = ["Noodles", "Egg rolls", "Milk", "Rice", "Soda", "Chips"]
print(shopping_list[2])
print(len(shopping_list))

# Going through a list
for item in shopping_list:
    print(item)

for num in the_count:
    print(num * 2)

len(shopping_list)  # Gives me the length of the shopping list
range(3)  # Gives a list of the numbers 0 through 2
range(len(shopping_list))  # A list of EVERY index in a list

for num in range(len(shopping_list)):
    item = shopping_list[num]
    print("The item at index %d is %s" % (num, item))


# Turn things into a list
str1 = "Hello Class!"
listOne = list(str1)
print(listOne)
listOne[11] = '.'
print(listOne)
print("".join(listOne))

# Add things to a list
shopping_list.append("Cereal, " "Cheese")
print(shopping_list)

# Removing things from a list
shopping_list.remove("Soda")
print(shopping_list)
shopping_list.pop(0)
print(shopping_list)

# The string class
print(string.ascii_letters)
print(string.ascii_lowercase)
print(string.punctuation)
print(string.digits)

# Dealing with strings
strTwo = "ThIs Is A vEry Odd SEntEncE"
lowercase = strTwo.lower()
print(lowercase)
