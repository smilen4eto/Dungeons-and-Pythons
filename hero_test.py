from hero import Hero

import unittest


class TestHero(unittest.TestCase):
    def setUp(self):
        self.bron_hero = Hero("Bron", 100, "Dragonslayer")

    def test_hero_init(self):
        self.assertEqual(self.bron_hero.name, "Bron")
        self.assertEqual(self.bron_hero.health, 100)
        self.assertEqual(self.bron_hero.nickname, "Dragonslayer")

    def test_known_as(self):
        self.assertEqual(self.bron_hero.known_as(), 'Bron the Dragonslayer')

    def test_get_health(self):
        self.assertEqual(100, self.bron_hero.get_health())

    def test_is_alive(self):
        self.assertTrue(self.bron_hero.is_alive())

    def test_is_dead(self):
        self.bron_hero.health = 0
        self.assertFalse(self.bron_hero.is_alive())

    def test_take_damage_in_the_limit(self):
        self.bron_hero.take_damage(50)
        self.assertEqual(50, self.bron_hero.take_damage(50))

    def test_take_damage_float(self):
        self.bron_hero.damage_points = 46.47
        self.assertEqual(53.53, self.bron_hero.take_damage(self.bron_hero.damage_points))

    def test_take_damage_False(self):
        self.bron_hero.damage_points = 300
        self.assertFalse(self.bron_hero.take_damage(self.bron_hero.damage_points))

    def test_take_healing(self):
        self.bron_hero.take_healing(20)
        self.bron_hero.health = 74
        self.assertTrue(self.bron_hero.take_healing(45))

    def test_take_healing_dead(self):
        self.bron_hero.take_healing(45)
        self.bron_hero.health = 0
        self.assertFalse(self.bron_hero.take_healing(45))





if __name__ == '__main__':
    unittest.main()
