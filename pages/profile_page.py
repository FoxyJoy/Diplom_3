from asyncio import timeout

import allure
from utils.urls import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from locators.locators import *
from selenium.webdriver.common.by import By
import time
from selenium.common.exceptions import TimeoutException

class ProfilePage(BasePage):
    @allure.step('Клик по кнопке личного кабинета')
    def click_profile_cabinet_button(self):
        # self.wait_for_invisible(LoginLocators.invisible_modal, 50)
        time.sleep(1)
        self.move_to_element_and_click(LoginLocators.cabinet)

    @allure.step('Клик по надписи регистрация')
    def click_registration_text_link(self):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(LoginLocators.register_text_link)).click()

    @allure.step('Ввод ия в поле "Имя"')
    def enter_name(self, name: str):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginLocators.name_input)).send_keys(name)

    @allure.step('Ввод почты в поле "Почта"')
    def enter_email(self, email: str):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LoginLocators.email_label)).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginLocators.email_input)).send_keys(email)

    @allure.step('Ввод пароля в поле "Пароль"')
    def enter_password(self, password: str):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LoginLocators.password_label)).click()
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(LoginLocators.password_input)).send_keys(password)

    @allure.step('Нажать на кнопку "Зарегистрироваться"')
    def click_registration_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LoginLocators.register_button)).click()

    @allure.step('Нажать на кнопку "Войти"')
    def click_login_button(self):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(LoginLocators.login_button)).click()

    @allure.step('Регистрируемся')
    def enter_registration_data(self):
        self.enter_name(self.name)
        self.enter_email(self.email)
        self.enter_password(self.password)
        self.click_registration_button()

    @allure.step('Вводи почту и пароль')
    def enter_login_data(self):
        self.enter_email(self.email)
        self.enter_password(self.password)
        self.click_login_button()

    @allure.step('Нажать на кнопку "История заказов"')
    def click_history_orders_button(self):
        self.click_on_element(ProfilePageLocators.order_history_button)

    @allure.step('Проверка отображения формы личного кабинета')
    def check_profile_area_form(self):
        return self.check_element(ProfilePageLocators.profile_form)

    @allure.step('Ожидание кнопки Отмена')
    def wait_cancel_button(self):
        self.find_element_clickable(ProfilePageLocators.save_button)

    @allure.step('Ждём, пока элемент станет видимым и перейдем в профиль')
    def go_to_profile(self):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((By.XPATH, "//a[text()='Личный кабинет']"))).click()

    @allure.step('Проверка отображения формы "Личного кабинета"')
    def check_authorization_form_cabinet(self):
        return self.check_element(*ProfilePageLocators.profile_button)


    @allure.step('Нажать на кнопку "Профиль"')
    def click_profile_button(self):
        self.click_on_element(*ProfilePageLocators.profile_button)

    @allure.step('Проверка наличия формы авторизации')
    def check_authorization_form(self):
        return self.check_element(LoginLocators.auth_form)

    @allure.step('Нажать на кнопку "Выход"')
    def click_exit_button(self):
        self.click_on_element(ProfilePageLocators.exit_button)

    @allure.step('Нажать на кнопку "Отмена"')
    def click_cansel_button(self):
        self.click_on_element(*ProfilePageLocators.exit_button)

    @allure.step('Нажать на кнопку "Сохранить"')
    def click_save_button(self):
        self.click_on_element(*ProfilePageLocators.save_button)

    @allure.step('Нажатие на ссылку "Восстановить пароль"')
    def click_recovery_button(self):
        self.move_to_element_and_click(PasswordPageLocators.link_recovery_button)

