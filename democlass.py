class test:
    a=10
    b=20
    c=30
    d=40
    def add(self):
        print(self.a+self.c)
    def sub(self):
        print(self.a-self.c)
    def mul(self):
        print(self.c-self.a)

t=test()
t.add()
t.sub()
t.mul()

class student:
    a=10
    b=5
    global d
    d=100
    def __add__(self):
        d=50
        c=self.a+self.b
        print(c)
        print(globals()['d'])
        print(d)
ankita=student()
deep=student()
manish=student()

ankita.add()
deep.add()
manish.add()
print(d)
print(ankita.a)

help(student)

class test:
    a=10
    b=5
    def mul(self):
        c=self.a+self.b
        print(c)
        print(self.a+self.b)
    def mul(self):
        print(self.a+self.b)

t=test()
t1=test()
t3=test()
t.mul()
t1.mul()
t3.mul()

class testinit:
    a=10
    b=20
    c=30
    def __init__(self):
        d=self.a+self.b+self.c
        print(d)
        print(self.a+self.b+self.c)

t=testinit()
t2=testinit()