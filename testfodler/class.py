class Animal:

    leg = 0

    def __init__(self, name, legs):
        print("Animal")
        self.animal_name = name
        self.legs=legs

    def make_sound(self, sound):
        print(f"{self.animal_name} makes {sound} sound")

    def has_legs(self):
        print(f"{self.animal_name} has {self.legs} legs")



class Dog(Animal):
    pass


terry = Dog("Terry", 3)

terry.make_sound("Woof!")
terry.has_legs()


# class Animal:
# Creates a class called Animal.
# A class is a blueprint used to create objects.

# leg = 0
# This is a class variable.
# It belongs to the Animal class and can be accessed by its objects.

# def __init__(self, name):
# __init__ is a special method called automatically
# when a new object is created.
#
# self refers to the current object.
# name is the value passed when creating the object.

# print("Animal")
# Prints "Animal" when the object is created.

# self.animal_name = name
# Creates an instance variable called animal_name.
# It stores the name of the specific object.
#
# For example:
# Dog("Terry")
#
# name = "Terry"
# self.animal_name = "Terry"

# def make_sound(self, sound):
# Creates a method called make_sound.
# A method is a function that belongs to a class.
#
# self refers to the object calling the method.
# sound is the value passed to the method.

# print(f"{self.animal_name} makes {sound} sound")
# Prints the animal's name and the sound it makes.
#
# self.animal_name gets the name stored in the object.
# sound gets the sound passed to the method.

# class Dog(Animal):
# Creates a Dog class.
#
# Dog inherits from Animal.
# This means Dog can use the methods and variables
# defined inside Animal.

# pass
# Means there is currently no additional code inside Dog.
# Dog still gets the functionality of Animal through inheritance.

# terry = Dog("Terry")
# Creates an object/instance of the Dog class.
# The object is stored in the variable called terry.
#
# "Terry" is passed to the __init__() method.
# Therefore:
# self.animal_name = "Terry"

# terry.make_sound("Woof!")
# Calls the make_sound() method using the terry object.
# "Woof!" is passed as the sound.
#
# Output:
# Terry makes Woof! sound


# KEY CONCEPTS
#
# Class:
# A blueprint for creating objects.
#
# Object / Instance:
# A specific thing created from a class.
#
# Method:
# A function that belongs to a class.
#
# Attribute:
# A variable/data that belongs to an object or class.
#
# self:
# Refers to the current object.
#
# Inheritance:
# Allows one class to get functionality from another class.
#
# Animal = Parent class
# Dog = Child class
# terry = Instance/Object of Dog
# Super= this is use to refer object from the parent class
