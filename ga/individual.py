# -*- coding: utf-8 -*-
"""
Created on Sat Mar 23 06:08:57 2019

@author: Khoi To
"""


class Individual(object):
    def __init__(self, chromosome, fitness_score=None):
        self.chromosome = chromosome
        self.fitness_score = fitness_score
