from trueskill import Rating


class Player(object):
    
    def __init__(self, name, rating):
        self.name = name
        self.history = []
        self.rating = Rating(rating)
        
    @property
    def losing_streak(self):
        streak = 0
        
        if len(self.history) == 0:
            return streak
        for i in range(len(self.history) - 1, -1, -1):
            if self.history[i] == 0:
                streak += 1
            else:
                return streak
        return streak
