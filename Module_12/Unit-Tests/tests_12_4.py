import logging
import unittest
from rt_with_exceptions import Runner

logging.basicConfig(level=logging.INFO, filemode='w', filename='runner_tests.log',
                    encoding='utf-8', format='%(message)s | %(levelname)s | %(asctime)s')
class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены.")
    def test_walk(self):
        '''
        Test runner walk
        :return:
        '''
        try:
            self.some_runner = Runner('Акакий', speed=(-5))
            logging.info('"test_walk" выполнен успешно.')
            # for i in range(10):
            #     self.some_runner.walk()
            # self.assertEqual(self.some_runner.distance, 50)
        except ValueError:
            logging.error("Неверная скорость для Runner.", exc_info=True)

    @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены.")
    def test_run(self):
        '''
        Test runner run
        :return:
        '''
        try:
            self.some_runner = Runner(1)
            logging.info('"test_run" выполнен успешно.')
            # for i in range(10):
            #     self.some_runner.run()
            # self.assertEqual(self.some_runner.distance, 100)
        except TypeError:
            logging.error('Неверный тип данных для объекта Runner.', exc_info=True)

    # @unittest.skipIf(is_frozen, "Тесты в этом кейсе заморожены.")
    # def test_challenge(self):
    #     '''
    #     Test runners not equal
    #     :return:
    #     '''
    #     self.some_runner1 = Runner('Акакий')
    #     self.some_runner2 = Runner('НонАкакий')
    #     for i in range(10):
    #         self.some_runner1.run()
    #         self.some_runner2.walk()
    #     self.assertNotEqual(self.some_runner1.distance, self.some_runner2.distance)

if __name__ == '__main__':


    unittest.main()
