# create protected class: protected vs private
class Protected:
    def __init__(self): # establishing values for protected and private variables 
        self._varProtected = 0 
        self.__varPrivate = 29

    def getPrivate(self):
        print(self.__varPrivate)

    def setPrivate(self, private): # created method for ability to change value of varPrivate
        self.__varPrivate = private

obj = Protected()
obj._varProtected = 13 # protected variable can be changed without creation of a new method
print(obj._varProtected) 

obj_2 = Protected()
obj_2.getPrivate() # call on getPrivate method for variable value
obj_2.setPrivate(30) # call setPrivate method to change variable value
obj_2.getPrivate() # display that value has changed
