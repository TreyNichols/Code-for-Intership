# The patient class has a name, age, and weight. Only the name and age
# are provided as arguments to the constructor. The weight is set to 150
# by default for all objects. A Patient also has an increaseAge function
# that increases the age by 1.

class Patient():

    #constructor 
    def __init__(self, name, age, weight = 150):
        self.name = name
        self.age = age
        self.weight = weight
        self.stay = stay

    #accessor for name
    @property
    def name(self):
        return self._name

    #mutator for name
    @name.setter
    def name(self, value):
        self._name = value

    #accessor for age
    @property
    def age(self):
        return self._age
    
    #mutator for age
    @age.setter
    def age(self, value):
        if (value<0):
            self._age = 0

        else:
            self._age = value

    #accessor for weight
    @property
    def weight(self):
        return self._weight
    
    #mutator for weight
    @weight.setter
    def weight(self, value):
        if (value<=0):
            self._weight = 150

        elif (value>=1400):
            self._weight = 150

        else:
            self._weight = value


class In():


    #constructor
    def __init__(self, name, age, weight = 150):
        self.name = name
        self.age = age
        self.weight = weight
        self.stay = stay

    #accessor for name
    @property
    def name(self):
        return self._name

    #mutator for name
    @name.setter
    def name(self, value):
        self._name = value

    #accessor for age
    @property
    def age(self):
        return self._age
    
    #mutator for age
    @age.setter
    def age(self, value):
        if (value<0):
            self._age = 0

        else:
            self._age = value

    #accessor for weight
    @property
    def weight(self):
        return self._weight
    
    #mutator for weight
    @weight.setter
    def weight(self, value):
        if (value<=0):
            self._weight = 150

        elif (value>=1400):
            self._weight = 150

        else:
            self._weight = value

    #accessor for stay
    @property
    def stay(self):
        return self._stay

    #mutator for stay
    @stay.setter
    def stay(self, value):
        if (value > 0):
            range(0,6)
            return stay

    #Out Constuctor
class Out():


    #constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.weight = weight
        self.stay = stay

    #accessor for name
    @property
    def name(self):
        return self._name

    #mutator for name
    @name.setter
    def name(self, value):
        self._name = value

    #accessor for age
    @property
    def age(self):
        return self._age
    
    #mutator for age
    @age.setter
    def age(self, value):
        if (value<0):
            self._age = 0

        else:
            self._age = value



class ICU():

    #constructor
    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.weight = weight
        self.stay = stay

    #accessor for name
    @property
    def name(self):
        return self._name

    #mutator for name
    @name.setter
    def name(self, value):
        self._name = value

    #accessor for age
    @property
    def age(self):
        return self._age
    
    #mutator for age
    @age.setter
    def age(self, value):
        if (value<0):
            self._age = 0

        else:
            self._age = value


    #accessor for weight
    @property
    def weight(self):
        return self._weight
    
    #mutator for weight
    @weight.setter
    def weight(self, value):
        if (value<=0):
            self._weight = 150

        elif (value>=1400):
            self._weight = 150

        else:
            self._weight = value


    #accessor for stay
    @property
    def stay(self):
        return self._stay

    #mutator for stay
    @stay.setter
    def stay(self, value):
        if (value > 0):
            range(0,6)
            return stay

    




class CheckUp():


    #constructor
    def __init__(self, CheckUp):
        self.CheckUp = CheckUp

    #accessor for Checkup
    @property
    def CheckUp(self):
        return self._CheckUp

    #mutator for CheckUp
    @CheckUp.setter
    def CheckUp(self, value):
        self.CheckUp = value

    
    #incriments age by 1 
    def increaseAge(self):
        self.age = int(self.age) + 1 
        


# Create three patient objects and print them out
p1 = ICU("Ben Dover", 5)
p2 = ICU("Helen Hywater", -15)
p3 = CheckUp("Amanda Lynn", 45)
p4 = ICU("Chester Minit", 12)
p5 = In("Don Keigh", 89, 10)
p6 = Out("Kay Oss ", 45)
print ("\tStatus\tName\t\tAge\tWeight\tStay")
print ("-" * 55)
print ("p1:\t{}".format(p1))
print ("p2:\t{}".format(p2))
print ("p3:\t{}".format(p3))
print ("p4:\t{}".format(p4))
print ("p5:\t{}".format(p5))
print ("p6:\t{}".format(p6))

print ("-" * 55)

# Change their ages and print them out
p1.age = -5
p2.age = 100
for i in range(6):
    p3.increaseAge()
p4.age = 0
p5.increaseAge()
p6.age = 42

print ("p1:\t{}".format(p1))
print ("p2:\t{}".format(p2))
print ("p3:\t{}".format(p3))
print ("p4:\t{}".format(p4))
print ("p5:\t{}".format(p5))
print ("p6:\t{}".format(p6))
print ("-" * 55)

# Change other instance variables and print them out
p1.weight = 2000
p1.stay = 3
p2.name = "Justin Thyme"
p2.weight = 220
p2.stay = 0
p3.weight = -50
p4.weight = 1400
p5.weight = 0
p5.stay = 21
p6.weight = 1401

print ("p1:\t{}".format(p1))
print ("p2:\t{}".format(p2))
print ("p3:\t{}".format(p3))
print ("p4:\t{}".format(p4))
print ("p5:\t{}".format(p5))
print ("p6:\t{}".format(p6))
print ("-" * 55)
