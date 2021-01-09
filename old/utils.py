from player import Player

import numpy as np


def generate_population(k=100):
    """Create a population of players.
    
    Players are instantiated with a skill level.
    """
    population = {}
    for i in range(k):
        rating = np.random.normal(loc=50.0, scale=10.0)
        population[i] = Player(i, rating=rating)
    return population