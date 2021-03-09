# create a parent/child class relationship using abstraction method

from abc import ABC, abstractmethod

class Food(ABC): # created parent/abstract class
    def Eat(self, edible):
        print("You can eat {}!".format(edible))

    @abstractmethod
    def Amount(self, count):
        pass

class Fruit(Food): # created child class
    def Amount(self, count): # define abstract method of parent class
        print('{} is the perfect amount of fruit to eat.'.format(count))

obj = Fruit()
obj.Eat("Apples") # implemented regular method
obj.Amount(2) #implemented abstract method
    
