# Create two classes that inherit from another class

class Employee: # parent class created 
    ID = 0
    name = ''
    email = ''
    phone = ''

class Department(Employee): # child class 1 created 
    Dep_ID = 0
    Dep_Title = ''

class Pay(Employee): # child class 2 created 
    Hours = 0
    Rate = 12.00
    
