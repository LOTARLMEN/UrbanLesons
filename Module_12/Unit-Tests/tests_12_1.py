import unittest
from runner import Runner


class RunnerTest(unittest.TestCase):
    def test_walk(self):
        '''
        Test runner walk
        :return:
        '''
        self.some_runner = Runner('Акакий')
        for i in range(10):
            self.some_runner.walk()
        self.assertEqual(self.some_runner.distance, 50)
    def test_run(self):
        '''
        Test runner run
        :return:
        '''
        self.some_runner = Runner('Акакий')
        for i in range(10):
            self.some_runner.run()
        self.assertEqual(self.some_runner.distance, 100)

    def test_challenge(self):
        '''
        Test runners not equal
        :return:
        '''
        self.some_runner1 = Runner('Акакий')
        self.some_runner2 = Runner('НонАкакий')
        for i in range(10):
            self.some_runner1.run()
            self.some_runner2.walk()
        self.assertNotEqual(self.some_runner1.distance, self.some_runner2.distance)

    # def test_challenge2(self):
    #     '''
    #     Test runners equal
    #     :return:
    #     '''
    #     self.some_runner1 = Runner('Акакий')
    #     self.some_runner2 = Runner('Акакий')
    #     for i in range(10):
    #         self.some_runner1.run()
    #         self.some_runner2.walk()


if __name__ == '__main__':
    unittest.main()