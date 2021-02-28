

# parent class
class Organism:
    name = 'Unknown'
    species = 'Unknown'
    legs = None
    arms = None
    dna = "Sequence A"
    origin = "Unknown"
    carbon_based = True

    def information(self):
        msg = "\nName: {} \nSpecies: {} \nLegs: {} \nArms: {} \n DNA: \nOrigin: {} \nCarbon Based: {}".format(self.name,self.species,self.legs,self.arms,self.dna,self.carbon_based)
        return msg

# child class instance
class Human(Organism):
    name = 'MacGyver'
    species = 'Homosapien'
    legs = 2
    arms = 2
    orgin = 'Earth'

    def ingenuity(self):
        msg = '\nCreates a deadly weaponmusing only a paper clip, chewing gum, and a roll of duct tape!'
        return msg


# another child class instance
class Dog(Organism):
    name = 'Spot'
    canine = 'Canine'
    legs = 4
    arms = 0
    dna = "Sequence B"
    origin = 'Earth'

    def bite(self):
        msg = "\nEmits a loud, menacing growl and bites down ferociously on it's target!"
        return msg

# another child class instance
class Bacterium(Organism):
    name = 'X'
    species = 'Bacteria'
    legs = 0
    arms = 0
    dna = "Sequence C"
    origin = 'Mars'

    def replication(self):
        msg = "\nThe cell began to divide and multiply into two separate organisms!"
        return msg







if __name__ == "__main__":
    human = Human() 
    print(human.information()) # call on inheritance info
    print(human.ingenuity()) # call on specific human method

    dog = Dog()
    print(dog.information()) # call on inheritance info
    print(dog.bite()) # call on dog specific method

    bacteria = Bacterium()
    print(bacteria.information()) # call on inhertiance info
    print(bacteria.replication()) # call on Bacterium specific method
    
