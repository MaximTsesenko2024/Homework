import runner
import unittest


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        test_run = runner.Runner('Denis')
        for _ in range(10):
            test_run.walk()
        self.assertEqual(test_run.distance, 50, 'Функция walk не работает')

    def test_run(self):
        test_run = runner.Runner('Denis')
        for _ in range(10):
            test_run.run()
        self.assertEqual(test_run.distance, 100, 'Функция run не работает')

    def test_challenge(self):
        test1 = runner.Runner('Denis')
        test2 = runner.Runner('Alex')
        for _ in range(10):
            test1.run()
            test2.walk()
        self.assertNotEqual(test1.distance, test2.distance, 'Функции run и walk одинаковы')


if __name__ == '__main__':
    unittest.main()
