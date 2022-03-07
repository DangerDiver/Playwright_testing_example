import os
import time
from datetime import datetime

from playwright.sync_api import sync_playwright

import settings as s


def login():
    # Initiate session
    s.playwright = sync_playwright().start()
    s.browser = s.playwright.chromium.launch(args=['--start-maximized'], headless=False, slow_mo=50)
    s.page = s.browser.new_page(no_viewport=True)

    # Open URL and login
    s.page.goto(s.url)
    s.page.fill('//input[@name = "username"]', s.username)
    s.page.fill('//input[@name = "password"]', s.password)
    s.page.locator("//input[@type='submit']").click()

    # Wait for page to load by waiting for text "Search" to appear
    s.page.locator('text=Open New Account').wait_for()


def logout():
    s.page.locator("//a[contains(text(), 'Log Out')]").click()
    s.browser.close()
    s.playwright.stop()


def wait(seconds):
    time.sleep(seconds)


def generateScreenshot(test_name, dirTestScreenshots):
    try:
        imgdir = dirTestScreenshots
        imgpath = ''
        if imgdir:
            x = str(test_name).split()
            tf = x[0]
            tc = x[1].split('.')[1][:-1]
            tt = datetime.now().strftime("%Y%m%d_%H%M%S")
            imgpath = os.path.join(imgdir, "%s-%s-%s.png" % (tc, tf, tt))
            s.page.screenshot(path=imgpath)
            # print("Test Screenshot:" + str(imgpath))
            print("Test Screenshot:" + "%s-%s-%s.png" % (tc, tf, tt))
        return imgpath
    except:
        print("Couldnt take a screenshot")
