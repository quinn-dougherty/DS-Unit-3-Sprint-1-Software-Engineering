#!/usr/bin/env python
'''python module for simulating aquariums'''

from collections import defaultdict

class Aquarium:
    '''Example class to model an aquarium'''
    def __init__(self, name="Pierre's Underwater World"):
        self.name = name
        self.fish = defaultdict(int)
    
    def add_fish(self,fish_species): 
        '''incrementing the count for fish_species in fish dict'''
        assert isinstance(fish_species, str)
        self.fish[fish_species] += 1
        pass

    def generate_fish_report(self): 
        '''iterate over and summarize self.fish dict'''
        for species, count in self.fish.items(): 
            print(f'{species}: {count}')

class Habitat: 
    def __init__(self, name="some habitat"): 
        self.name = name
        self.animals = defaultdict(int)
        self.plants = defaultdict(int)

    def generate_animal_report(self): 
        print('ANIMALS IN ' + self.name)
        for species, count in self.animals.items(): 
            print(f'{species}: {count}')

    def generate_plant_report(self): 
        print('PLANTS IN ' + self.name)
        for species, count in self.plants.items(): 
            print(f'{species}: {count}')

    def add_animals(self,animal_species): 
        '''incrementing the count for fish_species in fish dict'''
        assert isinstance(animal_species, str)
        self.animals[animal_species] += 1
        pass

    def add_plants(self,plant_species): 
        '''incrementing the count for plant_species in plants dict'''
        assert isinstance(plant_species, str)
        self.plants[plant_species] += 1
        pass


class Zoo(Habitat):
    '''Class to represent data and behavior of a zoo'''
    pass
