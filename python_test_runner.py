
from datetime import *
import unittest
import HtmlTestRunner
from unittest import TestCase
from Playwright_tests import *


class TestSolver(TestCase):
    # initialize the test suite
    loader = unittest.TestLoader()
    test_suite = unittest.TestSuite()
    outfile_py = os.getcwd()

    ## Playwright Tests

    now = (str(datetime.now())[:19]).replace(" ", "_").replace(":", "-")

    # test_suite.addTests(loader.loadTestsFromTestCase(Playwright_tests))
    test_suite.addTests(loader.loadTestsFromName('Playwright_tests.Playwright_tests.test_02_transfer_money'))

    runner_py = HtmlTestRunner.HTMLTestRunner(output=outfile_py, combine_reports=True,
                                              report_name="Playwright_Report_PyTest", add_timestamp=True)
    result_py = runner_py.run(test_suite)