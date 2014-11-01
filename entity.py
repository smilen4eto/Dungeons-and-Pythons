class Entity:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self.max_health = self.health
        self.weapon = None

    def get_health(self):
        return self.health

    def is_alive(self):
        return self.health > 0

    def take_damage(self, damage_points):
        self.damage_points = damage_points
        if self.damage_points < self.health:
            self.health = self.health - self.damage_points
        elif self.damage_points > self.health:
            self.health = 0
        return self.health

    def take_healing(self, healing_points):
        state = False
        if self.health > 0:
            state = True
            self.health += healing_points
            if self.health > self.max_health:
                self.health = self.max_health
        elif self.health < 0:
            state = False
        return state

    def has_weapon(self):
        if self.weapon is not None:
            return True
        else:
            return False

    def weapon_equip(self, weapon):
        self.weapon = weapon

    def attack(self):
        if self.weapon is None:
            return 0
        else:
            return 1