from unittest import *
import unittest
from SeleniumAutomation.Reports import HTMLTestRunner
from SeleniumAutomation.TestCases.Test_Retail_Login import *


if __name__ == '__main__':
    loader = unittest.TestLoader()
    suite = unittest.TestSuite((
        loader.loadTestsFromTestCase(Test_Retail_Login)))
    outfile = open('Report.html', 'w')
    runner = HTMLTestRunner.HTMLTestRunner(stream=outfile,
                            verbosity=1,
                            title='LinkedIn Report',
                            description='This is a demo report')
    runner.run(suite)
