import unittest
import rt_with_exceptions
import logging

class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_walk(self):
        try:
            runner_1 = rt_with_exceptions.Runner('Danil', -9)
            for i in range(10):
                runner_1.walk()
            self.assertEqual(runner_1.distance, 50)
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning('Неверная скорость для Runner', exc_info=True)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_run(self):
        try:
            runner_2 = rt_with_exceptions.Runner(10)
            for i in range(10):
                runner_2.run()
            self.assertEqual(runner_2.distance, 100)
            logging.info('"test_walk" выполнен успешно')
        except:
            logging.warning('Неверный тип данных для объекта Runner')

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_challenge(self):
        runner_1 = rt_with_exceptions.Runner('Danil')
        runner_2 = rt_with_exceptions.Runner('Alex')
        for i in range(10):
            runner_1.walk()
            runner_2.run()
        self.assertNotEqual(runner_1.distance, runner_2.distance)

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log', 
                        encoding='utf-8', format='%(asctime)s | %(levelname)s | %(message)s')

if __name__ == '__main__':
    unittest.main()
