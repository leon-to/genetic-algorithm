# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 06:08:57 2019

@author: Khoi To
"""

from algo.crossover
from individual import Individual
from characteristics import Characteristics
from handler.population import PopulationHandler
from handler.fitness import FitnessHandler


class GeneticAlgorithmModel(object):
    def __init__(self,
                 characteristics,
                 population, 
                 fitness,
                 ):
        self.characteristics = characteristics
        
        if population!=None:
            self.population = population
        else:
            self.population = PopulationHandler(self.characteristics)
            
        if fitness!=None:
            self.fitness = fitness
        else:
            self.fitness = FitnessHandler(self.population)
        
    def train(self):
        pass