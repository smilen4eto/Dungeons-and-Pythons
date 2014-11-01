from orc import Orc

import unittest


class TestOrc(unittest.TestCase):

    def setUp(self):
        self.mega_orc = Orc("Megadeth", 100, 1.54)

    def test_orc_init(self):
        self.assertEqual(self.mega_orc.name, "Megadeth")
        self.assertEqual(100, self.mega_orc.health)
        self.assertEqual(1.54, self.mega_orc.berserk_factor)

    def test_orc_init_with_crazy_orc(self):
        #self.mega_orc.berserk_factor = 3.45
        self.assertEqual("Megadeth", self.mega_orc.name)
        self.assertEqual(100, self.mega_orc.health)
        self.assertEqual(1.54, self.mega_orc.berserk_factor)

    def test_orc_init_happy(self):
        #self.berserk_factor = 0.45
        self.assertEqual("Megadeth", self.mega_orc.name)
        self.assertEqual(100, self.mega_orc.health)
        self.assertEqual(1.54, self.mega_orc.berserk_factor)

    def test_get_health(self):
        self.assertEqual(100, self.mega_orc.get_health())

    def test_is_alive(self):
        self.assertTrue(self.mega_orc.is_alive())

    def test_is_dead(self):
        self.mega_orc.health = 0
        self.assertFalse(self.mega_orc.is_alive())

    def test_take_damage_in_the_limit(self):
        self.mega_orc.take_damage(50)
        self.assertEqual(50, self.mega_orc.take_damage(50))

    def test_take_damage_float(self):
        self.mega_orc.damage_points = 46.47
        self.assertEqual(53.53, self.mega_orc.take_damage(self.mega_orc.damage_points))

    def test_take_damage_False(self):
        self.mega_orc.damage_points = 300
        self.assertFalse(self.mega_orc.take_damage(self.mega_orc.damage_points))

    def test_take_healing(self):
        self.mega_orc.take_healing(20)
        self.mega_orc.health = 74
        self.assertTrue(self.mega_orc.take_healing(45))

    def test_take_healing_dead(self):
        self.mega_orc.take_healing(45)
        self.mega_orc.health = 0
        self.assertFalse(self.mega_orc.take_healing(45))

if __name__ == '__main__':
    unittest.main()
