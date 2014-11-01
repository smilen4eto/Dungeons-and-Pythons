from entity import Entity


class Orc(Entity):
    def __init__(self, name, health, berserk_factor):
        super().__init__(name, health)
        self.berserk_factor = berserk_factor
        if self.berserk_factor > 2:
            self.berserk_factor = 2
        if self.berserk_factor < 1:
            self.berserk_factor = 1

    def attack(self):
        if self.weapon is None:
            return 0
        else:
            return 1 + self.berserk_factor
