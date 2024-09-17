import runner_and_tournament as rt
import unittest


class TournamentTest(unittest.TestCase):

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

    def test_start1(self):
        tour = rt.Tournament(90, self.run_1, self.run_3)
        TournamentTest.all_results[1] = tour.start()
        self.assertTrue(TournamentTest.all_results[1][2] == 'Ник')

    def test_start2(self):
        tour = rt.Tournament(90, self.run_2, self.run_3)
        TournamentTest.all_results[2] = tour.start()
        self.assertTrue(TournamentTest.all_results[2][2] == 'Ник')

    def test_start3(self):
        tour = rt.Tournament(90, self.run_1, self.run_2, self.run_3)
        TournamentTest.all_results[3] = tour.start()
        self.assertTrue(TournamentTest.all_results[3][3] == 'Ник')


if __name__ == '__main__':
    unittest.main()
