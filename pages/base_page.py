import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.urls import Urls
from selenium.webdriver import ActionChains
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from locators.locators import *

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Идем к странице')
    def go_to_main_page(self):
        self.driver.get(Urls.url_main_page)

    @allure.step('Получение текущего URL страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Клик по элементу')
    def click_on_element(self, locator, timeout = 10):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator)).click()

    @allure.step('Жде загрузку элемента')
    def wait_for_loading_element(self, locator, timeout=5):
        WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator))

    @allure.step('Найти элемент clickable')
    def find_element_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator), message=f"Can't find element by locator {locator}")

    @allure.step('Найти элемент')
    def find_element(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located(locator), message=f"Can't find element by locator {locator}")

    @allure.step('Прокрутка к элементу и клик по нему')
    def move_to_element_and_click(self, locator):
        element =  WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    @allure.step('Проверка отображения элемента на странице')
    def check_element(self, locator):
        self.wait_for_loading_element(locator)
        return self.driver.find_element(*locator)

    @allure.step('Проверка, что элемент не отображается на странице')
    def check_element_is_not_visible(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.invisibility_of_element_located(locator))

    @allure.step('Перетаскивание элемента к целевому элементу')
    def drag_and_drop(self, element_one, element_two):
        element = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element_one))
        target = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(element_two))
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(element, target).perform()

    @allure.step('Получение текста элемента после ожидания его видимости')
    def get_text_locator(self, locator):
        return WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator)).text

    @allure.step('Получение списка текстов элементов после ожидания их видимости')
    def get_text_locators(self, locator):
         return WebDriverWait(self.driver, 10).until(EC.visibility_of_all_elements_located(locator))

    @allure.step('Ввод текста в поле после ожидания его кликабельности')
    def send_keys_to_field(self, locator, text):
        self.wait_for_element_clickable(locator)
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('Ожидание, пока элемент станет кликабельным')
    def wait_for_element_clickable(self, locator):
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))

    @allure.step('Ожидание, кнопка')
    def click_button(self, locator):
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
        element = WebDriverWait(self.driver, 20, ignored_exceptions=ignored_exceptions).until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].click();", element)

    @allure.step('Ожидание, дата')
    def enter_data(self, locator, data: str):
        ignored_exceptions = (NoSuchElementException, StaleElementReferenceException,)
        WebDriverWait(self.driver, 10,  ignored_exceptions=ignored_exceptions).until(EC.visibility_of_element_located(locator)).send_keys(data)

    @allure.step('Ожидание, текст')
    def wait_text(self, locator, text: str):
        WebDriverWait(self.driver, 10).until_not(EC.text_to_be_present_in_element(locator, text))

    @allure.step('Ожидание, login_page')
    def wait_login_page(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_all_elements_located(LoginLocators.login_button))

    @allure.step('Ожидание, registration_page')
    def wait_registration_page(self):
        WebDriverWait(self.driver, 15).until(EC.presence_of_all_elements_located(LoginLocators.register_button))