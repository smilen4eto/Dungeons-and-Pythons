from entity import Entity

import unittest


class TestEntity(unittest.TestCase):

    def setUp(self):
        self.entity_hero = Entity("Eliss", 100)

    def test_entity_init(self):
        self.assertEqual("Eliss", self.entity_hero.name)
        self.assertEqual(100, self.entity_hero.health)

    def test_get_health(self):
        self.assertEqual(100, self.entity_hero.get_health())

    def test_is_alive(self):
        self.assertTrue(self.entity_hero.is_alive())

    def test_is_dead(self):
        self.entity_hero.health = 0
        self.assertFalse(self.entity_hero.is_alive())

    def test_take_damage_in_the_limit(self):
        self.entity_hero.take_damage(50)
        self.assertEqual(50, self.entity_hero.take_damage(50))

    def test_take_damage_float(self):
        self.entity_hero.damage_points = 46.47
        self.assertEqual(53.53, self.entity_hero.take_damage(self.entity_hero.damage_points))

    def test_take_damage_False(self):
        self.entity_hero.damage_points = 300
        self.assertFalse(self.entity_hero.take_damage(self.entity_hero.damage_points))

    def test_take_healing(self):
        self.entity_hero.take_healing(20)
        self.entity_hero.health = 74
        self.assertTrue(self.entity_hero.take_healing(45))

    def test_take_healing_dead(self):
        self.entity_hero.take_healing(45)
        self.entity_hero.health = 0
        self.assertFalse(self.entity_hero.take_healing(45))

    def test_has_no_weapon(self):
        self.assertFalse(self.entity_hero.weapon)

    def test_has_weapon(self):
        self.entity_hero.weapon = "machete"
        self.assertTrue(self.entity_hero.weapon)

    def test_weapon_equipped(self):
        self.entity_hero.weapon_equip("dagger")
        self.assertEqual(self.entity_hero.weapon, "dagger")

    def test_damage_without_weapon(self):
        self.assertEqual(0, self.entity_hero.attack())



if __name__ == '__main__':
    unittest.main()
