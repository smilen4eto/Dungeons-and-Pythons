from weapon import Weapon

import unittest


class TestWeapon(unittest.TestCase):

    def setUp(self):
        self.mega_weapon = Weapon("machete", 45, 0.745)

    def test_weapon_init(self):
        self.assertEqual(self.mega_weapon.type, "machete")
        self.assertEqual(self.mega_weapon.damage, 45)
        self.assertEqual(self.mega_weapon.critical_strike_percent, 0.745)

    def test_critical_hit(self):
        hasCrited = False
        hasNotCrited = False

        for x in range(1, 1000):
            if self.mega_weapon.critical_hit():
                hasCrited = True
            else:
                hasNotCrited = True

        self.assertTrue(hasCrited and hasNotCrited)

if __name__ == '__main__':
    unittest.main()
