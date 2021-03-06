''' name (string with no default)
    price (integer with default value 10)
    weight (integer with default value 20)
    flammability (float with default value 0.5)
    identifier (integer, automatically genererated as a random (uniform) number anywhere from 1000000 to 9999999, includisve)(inclusive).


'''
from random import randint


def divide(x, y): return x / y


class Product:
    def __init__(
        self,
        name,
        price=10,
        weight=20,
        flammability=0.5,
        identifier=randint(
            1000000,
            9999999 + 1)):

        if isinstance(name, str):
            self.name = name
        if isinstance(price, int):
            self.price = price
        if isinstance(weight, int):
            self.weight = weight
        if isinstance(flammability, float):
            self.flammability = flammability
        if isinstance(identifier, int):
            self.identifier = identifier

    def stealability(self) -> str:
        '''no args just reads from state, returns string

        calculates the price divided by the weight, and then returns a
        message: if the ratio is less than 0.5 return "Not so
        stealable...", if it is greater or equal to 0.5 but less
        than 1.0 return "Kinda stealable.", and otherwise
        return "Very stealable!"'''
        assert self.weight != 0
        x = divide(self.price, self.weight)
        if x < 0.5:
            return "Not so stealable..."
        elif 0.5 <= x < 1:
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
        if x < 10:
            return "...fizzle."
        elif 10 <= x < 50:
            return "...boom!"
        else:
            return "...BABOOOM!"


class BoxingGlove(Product):
    '''Make a subclass of Product named BoxingGlove that does the following:

    Change the default weight to 10 (but leave other defaults unchanged)
    Override the explode method to always return "...it's a glove."
    Add a punch method that returns "That tickles." if the weight is
    below 5, "Hey that hurt!" if the weight is greater or equal to 5 but
    less than 15, and "OUCH!" otherwise
    '''

    def __init__(self,
                 name,
                 price=10,
                 weight=10,
                 flammability=0.5,
                 identifier=randint(
                     1000000,
                     9999999 +
                     1)):
        super().__init__(name, price, weight, flammability, identifier)

    def explode(self) -> str:
        return "...it's a glove."

    def punch(self) -> str:
        if self.weight < 5:
            return "That tickles."
        elif 5 <= self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"
