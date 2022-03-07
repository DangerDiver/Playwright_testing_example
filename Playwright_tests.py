
from unittest import TestCase

from base_methods import *


class Playwright_tests(TestCase):

    def setUp(self):
        # check start time
        s.tick = datetime.now()
        login()
        print("Start time: %s" % str(s.tick))

    def tearDown(self):

        generateScreenshot(self, s.failure_screenshot_dir)
        logout()
        s.tock = datetime.now()
        print("Stop time: %s" % str(s.tock))
        diff = s.tock - s.tick  # the result is a datetime.timedelta object
        time_taken = diff.total_seconds()
        print("Test execution time: %s sec" % time_taken)

    def test_01_check_login_successful(self):

        # Test summary
        print("Test Summary: Validate Successful Login\n")

        # Check if Name appears at avatar
        login_name = s.page.locator("//a[contains(text(), 'Open New Account')]").count()
        if login_name == 1:
            print("Username appears as expected")
        else:
            print("Username not appearing as expected, investigate")
            assert False

    def test_02_transfer_money(self):

        # Test summary
        print("Test Summary: Transfer money\n")

        # Click on "Transfer Funds"
        print('Click on "Transfer Funds"\n')
        s.page.locator("text=Transfer Funds").click()

        # Enter Amount
        print('Enter amount\n')
        s.page.fill("input#amount", "1500")

        # Click the transfer button
        print('Click the transfer button\n')
        s.page.locator('//input[@value = "Transfer"]').click()

        # Confirm transfer
        print('Confirm transfer\n')
        confirm_msg = s.page.locator("//h1[contains(text(), 'Transfer Complete!')]").count()

        if confirm_msg == 1:
            print("Transfer has been performed")
        else:
            print("Transfer has not been performed, investigate!")
            assert False