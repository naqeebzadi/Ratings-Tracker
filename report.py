import unittest
import HTMLTestRunner
import os
from Navigation import UserTest
from LogIn import LogInTest
direct = os.getcwd()

class MyTestSuite(unittest.TestCase):

    def test_Issue(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.TestLoader().loadTestsFromTestCase(LogInTest),
            unittest.TestLoader().loadTestsFromTestCase(UserTest)])


        outfile = open(direct + "\RatingsTrackerTestSummary.html", "w")

        runner1 = HTMLTestRunner.HTMLTestRunner(
            stream = outfile,
            title='Ratings Tracker Test Report',
            description=' Acceptance Tests')
        runner1.run(smoke_test)
        print('Test Report Generated')


if __name__ == '__main__':
    unittest.main()

