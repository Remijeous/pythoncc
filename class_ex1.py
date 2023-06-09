# -*- coding: utf-8 -*-
"""class_ex1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1yhj_3MxYbGDntyet16OfLRB8dOlK-rNb
"""

class Dog():
  """A simple attempt to model a dog."""
  def __init__(self, name, age):
    """Initialize name and age attributes."""
    self.name = name
    self.age = age

  def sit(self):
    """Simlulate a dog sitting in respond to a comment"""
    print(self.name.title() + " is now sitting.")

  def roll(self):
    print(self.name.title() + " is rolled over")

my_dog = Dog('willie', 6)
your_dog = Dog('lucy', 3)
#my_dog.sit()
#my_dog.roll()
print("My dog name is " + my_dog.name.title())
print("My dog age is " + str(my_dog.age) + " Years old")
my_dog.sit()

print("\nYour dog's name is " + your_dog.name.title() + ".")
print("Your dog age is " + str(your_dog.age) + " years old")
your_dog.roll()

class Restaurant():
  """Creating a Class for Restaurant"""

  def __init__(self, rest_name, cuisine_type):
    self.rest_name = rest_name
    self.cuisine_type = cuisine_type

  def describe_restaurant(self):
    print(self.rest_name.title() + " is very famous for its ambitience")

  def restaurant_open(self):
    print("This " + self.rest_name.title() + " Restaurant will open at 8am Everyday")

this_restaurant = Restaurant("le meridian", "italian")
that_restaurant = Restaurant("forbidden kingdom", "asian")

print("This restaurant name is " + this_restaurant.rest_name.title())
print("Cuisine Type is: " + this_restaurant.cuisine_type.title())
this_restaurant.describe_restaurant()
that_restaurant.restaurant_open()