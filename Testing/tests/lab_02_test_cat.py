from lab_02_cat import Cat

from unittest import TestCase, main


class TestCat(TestCase):
    def setUp(self):
        self.cat = Cat('Tom')

    def test_init_cat(self):
        self.assertEqual('Tom', self.cat.name)
        self.assertEqual(0, self.cat.size)
        self.assertFalse(self.cat.sleepy)
        self.assertFalse(self.cat.fed)

    def test_size_increased_after_eat(self):
        self.assertEqual(0, self.cat.size)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.cat.eat()
        self.assertEqual(1, self.cat.size)
        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)

    def test_raise_eat_already_fed(self):
        self.cat.fed = True
        self.assertTrue(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertTrue(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)
        self.assertEqual('Already fed.', str(ex.exception))

    def test_sleep_cat(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)

        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)
        self.assertTrue(self.cat.fed)

    def test_raises_sleep_if_not_fed(self):
        self.cat.sleepy = True
        self.assertFalse(self.cat.fed)
        self.assertTrue(self.cat.sleepy)

        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertFalse(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))


if __name__ == '__main__':
    main()
