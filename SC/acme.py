''' name (string with no default)
    price (integer with default value 10)
    weight (integer with default value 20)
    flammability (float with default value 0.5)
    identifier (integer, automatically genererated as a random (uniform) number anywhere from 1000000 to 9999999, includisve)(inclusive).


'''
from numpy.random import randint
from numpy import divide

class Product: 
    def __init__(self, name, price=10, weight=20, flammability=0.5, identifier=randint(1000000, 9999999+1)): 
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self) -> str: 
        '''no args just reads from state, returns string
        
        calculates the price divided by the weight, and then returns a 
        message: if the ratio is less than 0.5 return "Not so 
        stealable...", if it is greater or equal to 0.5 but less 
        than 1.0 return "Kinda stealable.", and otherwise 
        return "Very stealable!"'''
        x = divide(self.price, self.weight)
        if x<0.5: 
            return "Not so stealable..."
        elif x>=0.5 and x < 1: 
            return "Kinda stealable." 
        else: 
            return "Very stealable!"

    def explode(self) -> str: 
        '''no args, return string
        
        calculates the flammability times the weight, and then returns a 
        message: if the product is less than 10 return "...fizzle.", if it is 
        greater or equal to 10 but less than 50 return "...boom!", and 
        otherwise return "...BABOOM!!"
        '''
        x = self.flammability * self.weight
        if x<10: 
            return "...fizzle."
        elif x>=10 and x<50: 
            return "...boom!"
        else: 
            return "...BABOOOM!"



