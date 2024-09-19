import runner
import runner_and_tournament as rt
import unittest


class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @classmethod
    def tearDownClass(cls):
        for key, val in cls.all_results.items():
            for i in val.keys():
                print(i, val[i], sep=':', end=' ')
            print('')

    def setUp(self):
        self.run_1 = rt.Runner('Усэйн', 10)
        self.run_2 = rt.Runner('Андрей', 9)
        self.run_3 = rt.Runner('Ник', 3)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start1(self):
        tour = rt.Tournament(90, self.run_1, self.run_3)
        TournamentTest.all_results[1] = tour.start()
        self.assertTrue(TournamentTest.all_results[1][2] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start2(self):
        tour = rt.Tournament(90, self.run_2, self.run_3)
        TournamentTest.all_results[2] = tour.start()
        self.assertTrue(TournamentTest.all_results[2][2] == 'Ник')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_start3(self):
        tour = rt.Tournament(90, self.run_1, self.run_2, self.run_3)
        TournamentTest.all_results[3] = tour.start()
        self.assertTrue(TournamentTest.all_results[3][3] == 'Ник')


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        test_run = runner.Runner('Denis')
        for _ in range(10):
            test_run.walk()
        self.assertEqual(test_run.distance, 50, 'Функция walk не работает')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        test_run = runner.Runner('Denis')
        for _ in range(10):
            test_run.run()
        self.assertEqual(test_run.distance, 100, 'Функция run не работает')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test1 = runner.Runner('Denis')
        test2 = runner.Runner('Alex')
        for _ in range(10):
            test1.run()
            test2.walk()
        self.assertNotEqual(test1.distance, test2.distance, 'Функции run и walk одинаковы')


if __name__ == '__main__':
    unittest.main()
