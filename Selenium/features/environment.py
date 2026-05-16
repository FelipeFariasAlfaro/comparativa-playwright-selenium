import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service


def _create_driver():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--log-level=3")
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    service = Service(log_output=os.devnull)
    driver = webdriver.Chrome(options=options, service=service)
    driver.implicitly_wait(10)
    return driver


def before_scenario(context, scenario):
    context.driver = _create_driver()


def after_scenario(context, scenario):
    context.driver.quit()
