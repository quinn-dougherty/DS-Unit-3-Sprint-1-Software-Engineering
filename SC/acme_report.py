'''Your module should include two functions:

    generate_products() should generate a given number of products (default 30), randomly, and return them as a list
    inventory_report() takes a list of products, and prints a "nice" summary

For the purposes of generation, "random" means uniform - all possible values should vary uniformly across the following possibilities:

    name should be a random adjective from ['Awesome', 'Shiny', 'Impressive',
    'Portable', 'Improved'] followed by a space and then a random noun from
    ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???'], e.g. 'Awesome Anvil' and Portable Catapult' are both possible
    price and weight should both be from 5 to 100 (inclusive and independent, and remember - they're integers!)
    flammability should be from 0.0 to 2.5 (floats)

You should implement only depending on random from the standard library, your Product class from acme.py, and built-in Python functionality.

For the report, you should calculate and print the following values:

    Number of unique product names in the product list
    Average (mean) price, weight, and flammability of listed products
'''


import numpy.random as rn
from numpy import divide as dv
from functools import reduce
from acme import Product

N = 30
ADJECTIVES = ['Awesome', 'Shiny', 'Impressive', 'Portable', 'Improved']
NOUNS = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']


def generate_products(n=N):
    '''Randomly generates a list of products.'''
    prods = [
        Product(
            name=f'{rn.choice(ADJECTIVES)} {rn.choice(NOUNS)}',
            price=rn.randint(
                5,
                100 + 1),
            weight=rn.randint(
                5,
                100 + 1),
            flammability=2.5 * rn.ranf())
        for _ in range(n)]
    return prods


def inventory_report(prod_list, n=N):
    s0 = "\nACME CORPORATION OFFICIAL INVENTORY REPORT\n"
    s1 = f'\nThere are {len(set([prod.name for prod in prod_list]))} unique names in this product list.\n\n'
    atts = ['price', 'weight', 'flammability']
    means = {atts[0]: dv(sum([prod.price for prod in prod_list]), n),
             atts[1]: dv(sum([prod.weight for prod in prod_list]), n),
             atts[2]: dv(sum([prod.flammability for prod in prod_list]), n)}

    s2 = [f'The mean {atts[k]} is {means[atts[k]]:.3}\n' for k in [0, 1, 2]]
    return s0 + s1 + reduce(lambda s, t: s + t, s2)


if __name__ == '__main__':
    print(inventory_report(generate_products()))
