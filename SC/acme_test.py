#!/usr/bin/env python
'''

Add at least 2 more test methods to AcmeProductTests for the base Product class:
    - at least 1 that tests default values (as shown), and one that builds an
      object with different values and ensures their stealability() and
      explode() methods function as they should
'''
import unittest
from acme import Product, BoxingGlove
from acme_report import generate_products, ADJECTIVES, NOUNS
from itertools import product as cart


def divide(x, y): return x / y


def exp(x): return 2 ** x


class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""

    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_prodct(self):
        """test all attributes and methods of default product"""
        prod = Product("default")
        self.assertEqual(prod.price, 10)
        self.assertAlmostEqual(prod.flammability, 0.5)
        self.assertEqual(prod.weight, 20)
        self.assertEqual(prod.stealability(), "Kinda stealable.")

    def test_explode(self):
        """test the explode method"""
        prod1 = Product('test prod 1', weight=400, flammability=400.0)
        prod2 = Product("not explosive", weight=1, flammability=exp(-4.0))
        #glove = BoxingGlove("adonis creed")
        self.assertEqual(prod1.explode(), "...BABOOOM!")
        self.assertEqual(prod2.explode(), "...fizzle.")
        #self.assertEqual(glove.explode(), "...it's a glove.")

    def test_stealability(self):
        """test stealability method"""
        very = Product('rocky', weight=1, price=exp(40))
        notatall = Product("rocks", weight=exp(40), price=1)
        self.assertEqual(very.stealability(), "Very stealable!")
        self.assertEqual(notatall.stealability(), "Not so stealable...")

    pass


class AcmeReportTests(unittest.TestCase):
    """test report

        - Write a new test class AcmeReportTests with at least 2 test methods:
      test_default_num_products which checks that it really does receive a
      list of length 30, and test_legal_names which checks that the
      generated names for a default batch of products are all valid possible
      names to generate (adjective, space, noun, from the lists of possible words)

"""

    def test_default_num_products(self):
        self.assertEqual(len(generate_products()), 30)

    def test_legal_names(self):
        full_prod = [' '.join(t) for t in cart(ADJECTIVES, NOUNS)]
        gen_names = [prod.name for prod in generate_products()]
        for n in gen_names:
            self.assertIn(n, full_prod)


if __name__ == '__main__':
    unittest.main()
