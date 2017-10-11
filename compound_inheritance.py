class A():
    def __init__(self,name):
        self.name=name
        print self.name,' Using Initialisation'
    def printA(self):
        print self.name, " Using Class Function"
class B(A):
    def printB(self):
        print self.name, " Using Class Function"
class C(B):
    def printC(self):
        print self.name, " Using Class Function"
class D(B):
    def printD(self):
        print self.name, " Using Class Function"
a=A("My name is A")
b=B("My name is B")
c=C("My name is C")
d=D("My name is D")
d.printD()