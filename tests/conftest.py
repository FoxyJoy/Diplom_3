import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions
from utils.urls import *

@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        options = ChromeOptions()
        options.page_load_strategy = 'normal'
        options.timeouts = {'implicit': 15000}
        options.timeouts = {'script': 50000}
        options.timeouts = {'pageLoad': 50000}
        options.unhandled_prompt_behavior = 'accept'
        driver = webdriver.Chrome(options=options)
        driver.maximize_window()
        driver.get(Urls.url_main_page)
    elif request.param == 'firefox':
        options = FirefoxOptions()
        options.page_load_strategy = 'normal'
        options.timeouts = {'implicit': 15000}
        options.timeouts = {'script': 50000}
        options.timeouts = {'pageLoad': 50000}
        options.unhandled_prompt_behavior = 'accept'
        driver = webdriver.Firefox(options=options)
        driver.maximize_window()
        driver.get(Urls.url_main_page)
    yield driver
    driver.quit()
