# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 06:08:57 2019

@author: Khoi To
"""

from abc import ABCMeta, abstractmethod

class Crossover(metaclass=ABCMeta):
    @abstractmethod
    def crossover(self, parent1, parent2):
        pass
        
class BasicCrossover(Crossover):
    def crossover(self, parent1, parent2):
        pass        