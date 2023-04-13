#object oriented definitions and terms
#
#
print(dir(list()))
#object is a bit of code and data
#objects - instance is anothr word for object.  ex> strings, intergers, float, list, dictionary

#class- a shape of an object, general characteristics of a thing (str)
#object-
#creating a class
class PartyAnimal:
    x = 0 #attribute saying all party animals will have a variable x = 0 in them
    def party(self): #method of party animal
        self.x = self.x + 1
        print("so far", self.x)
an = PartyAnimal() #same as x = list() an is a party animal object using the party animal template
an.party() #calls the party method, kind of like saying PartyAnimal.party.(an)
an.party()
an.party()
#so far 1
#so far 2
#so far 3

#method- the verbs of the python language .method()
#methods are an objects ability/ like calling a function inside of the object
dir(object) #what are the capabilities
#attribute-

#class

#how objects are built and thrown away
#constructors
#the primary purpose the constructor is to set up initial values
#outside we say make us one of these things but we need to get all the things inside of it right

class PartyAnimal:
    x = 0

    def __init__(self): #constructor (special black of statements that are called at the moment of creation..)
        print('I am constructed')

    def party(self):
        self.x = self.x + 1
        print(f'So far {self.x}')

    def __del__(self): #destructor
        print(f'I am destructed, last value of x = {self.x}')
an = PartyAnimal()
an.party()
an.party()
an = 42
print(f'an contains {an}')

#each time we stamp out an object like party animal we can change it to be its own little thing, with its own attributes and values

#multiple instances in when we make a bunch if objects from the same template
class PartyAnimal:
    x = 0
    name = ""

    def __init__(self,z):
        self.name = z
        print(self.name, 'Constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)

s = PartyAnimal("sally")
s.party()
j = partyanimal("Jim")
j.party()
s.party()

#object inheritance, we make more than one template
#make a class from an existing template and the add stuff to make our own class
#

class PartyAnimal:
    x = 0
    name = ""

    def __init__(self,nam): #whole point of this constructor is to just grab that name parameter
        self.name = nam
        print(self.name, 'Constructed')

    def party(self):
        self.x = self.x + 1
        print(self.name, "party count", self.x)

class Footballfan(PartyAnimal): #football fan is everything partyanimal is plus whatever we put down below
    points = 0
    def touchdown(self):
        self.points = self.points + 7
        self.party()
        print(self.name, "self", self.points)

j = Footballfan("jim")
j.party() #brings x to 1
j.touchdown() # brings points to 7
#footballfan has x=, name=, and points=

#class - template
#attribute - a variable within a classmethod
#object - a particular instance of a class
#constructor - code runs when an object is created
#inheritance - the ability to extend a class to make a new class
