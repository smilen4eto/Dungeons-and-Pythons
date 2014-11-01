import random


class Weapon:
    def __init__(self, type, damage, critical_strike_percent):
        self.type = type
        self.damage = damage
        self.critical_strike_percent = critical_strike_percent

    def critical_hit(self):
        random_number = random.random()
        if random_number < self.critical_strike_percent:
            return True
        return False
