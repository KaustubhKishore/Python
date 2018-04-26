class Animal():
    def __init__(self,name):
        self.name=name
    def talk(self) :
        print 'rooar!'
class Dog(Animal):
    def talk (self):
        print 'Woof ', self.name
class Cat(Animal):
    def talk(self):
        print 'Meow!'
a=Animal("Tom")
a.talk()
d=Dog("Gabe")
d.talk()
c=Cat("MM")
c.talk()
