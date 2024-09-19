import logging
import rt_with_exceptions as rt
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_walk(self):
        try:
            test_run = rt.Runner('Denis', -5)
            for _ in range(10):
                test_run.walk()
            self.assertEqual(test_run.distance, 50, 'Функция walk не работает')
            logging.info('"test_walk" выполнен успешно')
        except ValueError:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_run(self):
        try:
            test_run = rt.Runner(('Denis', 'Alex'))
            for _ in range(10):
                test_run.run()
            self.assertEqual(test_run.distance, 100, 'Функция run не работает')
            logging.info('"test_run" выполнен успешно')
        except TypeError:
            logging.warning('Неверный тип данных для объекта Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены')
    def test_challenge(self):
        test1 = rt.Runner('Denis')
        test2 = rt.Runner('Alex')
        for _ in range(10):
            test1.run()
            test2.walk()
        self.assertNotEqual(test1.distance, test2.distance, 'Функции run и walk одинаковы')


logging.basicConfig(level=logging.INFO, filemode='w', filename="runner_tests.log", encoding='UTF-8',
                    format="%(levelname)s | %(asctime)s | %(message)s")
if __name__ == '__main__':
    unittest.main()
