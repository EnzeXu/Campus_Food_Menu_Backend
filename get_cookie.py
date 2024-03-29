import sys
import os
import platform
import time
from selenium import webdriver
from datetime import datetime
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def chrome_driver(url, headless, chromedriver_path=None):
    chrome_options = webdriver.ChromeOptions()  # Options()
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('--no-sandbox')
    if headless:
        chrome_options.add_argument("--headless=new")
    if chromedriver_path is None:
        chromedriver_path = "{0}{1}{2}{3}{4}{5}{6}".format(
            sys.path[0], os.sep, "chromedriver", os.sep, platform.system().lower(), os.sep, "chromedriver")
    print(f"chormedriver path: {chromedriver_path}")
    service = ChromeService(executable_path=chromedriver_path)
    driver = webdriver.Chrome(options=chrome_options, service=service)
    # driver.maximize_window()
    # driver.implicitly_wait(3)
    driver.set_page_load_timeout(30)
    driver.set_script_timeout(30)
    # menuSkipLink
    # element = WebDriverWait(driver, 10).until(
    #     EC.presence_of_element_located((By.ID, "someElementId"))
    # )

    try:
        driver.get(url)
    except Exception as e:
        print("Error in loading page too slow:", e)
        driver.execute_script("window.stop()")
    return driver


def get_cookie(url, headless=True, chromedriver_path=None):
    driver = chrome_driver(url, headless, chromedriver_path)
    cookie_items = driver.get_cookies()
    cookie_str = ""
    for item_cookie in cookie_items:
        item_str = "{0}={1};".format(item_cookie["name"], item_cookie["value"])
        cookie_str += item_str
    driver.quit()
    return cookie_str


if __name__ == "__main__":
    # print(platform.system().lower())
    res = get_cookie("https://williamandmary.campusdish.com/api/menu/GetMenus?locationId=78391&mode=Daily&periodId=5409", True)
    print(res)