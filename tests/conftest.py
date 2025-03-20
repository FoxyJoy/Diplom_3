import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.chrome.options import Options as ChromeOptions

@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    if request.param == 'chrome':
        options = ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        driver = webdriver.Chrome(options=options)
        driver.get('https://stellarburgers.nomoreparties.site/')
    elif request.param == 'firefox':
        options = FirefoxOptions()
        options.add_argument("--width=1200")
        options.add_argument("--height=900")
        options.set_preference("browser.privatebrowsing.autostart", True)
        driver = webdriver.Firefox(options=options)
        driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver
    print("Закрываю браузер")  # Логирование
    driver.quit()
