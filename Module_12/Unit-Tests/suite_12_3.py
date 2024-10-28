import unittest
import tests_12_1
import tests_12_2


some_test = unittest.TestSuite()
some_test.addTest(unittest.TestLoader().loadTestsFromModule(tests_12_1))
some_test.addTest(unittest.TestLoader().loadTestsFromModule(tests_12_2))

runner = unittest.TextTestRunner(verbosity=2)

if __name__ == '__main__':
    runner.run(some_test)