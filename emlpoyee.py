class employee:
    def __init__(self, firstname, lastname, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.salary = salary
        self.email = self.firstname + self.lastname + "@gmail.com"

    def giveRaise(self, salary):
        self.salary = salary


class developer(employee):

    def __init__(self, firstname, lastname, salary, programming_language):
        super().__init__(firstname, lastname, salary)
        self.prog_langs = programming_language

    def addLauguage(self, lang):
        self.prog_langs += [lang]


employee1 = employee("Manish", "Jakhmola", 30000)

print(employee1.salary)
employee1.giveRaise(50000)
print(employee1.salary)
dev1 = developer("Tushar", "Sharma", 70000, ["Python", "Java"])
print(dev1.salary)
dev1.giveRaise(90000)
print(dev1.salary)
dev1.addLauguage("C++")
print(dev1.prog_langs)
