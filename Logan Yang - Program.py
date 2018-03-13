class Person(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def work(self):
        print("%s goes to work" % self.name)


class Employee(Person):
    def __init__(self, name, age, job):
        super(Employee, self).__init__(name, age)
        self.job = job

    def employed(self):
        print("%s is now employed" % self.name)


class Programmer(Employee):
    def __init__(self, name, age, job, income):
        super(Programmer, self).__init__(name, age, job)
        self.income = income

    def make_program(self):
        print("%s has made a program" % self.name)


jon = Employee("Jon", 23, "Salesman")
jon.employed()
ryan = Programmer("Ryan", 24, "Programmer", 5000)
ryan.make_program()
