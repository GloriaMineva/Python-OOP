from Testing.lab_01_worker import Worker
from unittest import TestCase, main

class TestWorker(TestCase):
    def test_init_worker(self):
        w = Worker('az', 1000, 50)
        self.assertEqual('az', w.name)
        self.assertEqual(1000, w.salary)
        self.assertEqual(50, w.energy)
        self.assertEqual(0, w.money)

    def test_rest_energy_increase(self):
        w = Worker('az', 1000, 50)
        self.assertEqual(50, w.energy)
        w.rest()
        self.assertEqual(51, w.energy)

    def test_work_worker_no_energy_raise(self):
        w = Worker('az', 100, 0)

        self.assertEqual(0, w.money)
        self.assertEqual(0, w.energy)

        with self.assertRaises(Exception) as ex:
            w.work()

        self.assertEqual(0, w.money)
        self.assertEqual(0, w.energy)
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_money_increased_work(self):
        w = Worker('az', 1000, 50)
        self.assertEqual(0, w.money)
        w.work()
        self.assertEqual(1000, w.money)
        w.work()
        self.assertEqual(2000, w.money)

    def test_energy_decrease_work(self):
        w = Worker('az', 1000, 50)
        self.assertEqual(50, w.energy)
        w.work()
        self.assertEqual(49, w.energy)

    def test_get_info(self):
        w = Worker('az', 1000, 50)
        self.assertEqual('az has saved 0 money.', w.get_info())
        w.work()
        self.assertEqual('az has saved 1000 money.', w.get_info())





if __name__ == '__main__':
    main()