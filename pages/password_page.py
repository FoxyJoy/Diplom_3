import allure
from pages.base_page import BasePage
from locators.locators import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class PasswordPage(BasePage):
    @allure.step('Проверка отображения формы восстановления пароля')
    def check_recovery_form(self):
        return self.check_element(PasswordPageLocators.recovery_text_form)

    @allure.step('Ввод Email в поле для электронной почты')
    def input_email_to_email_field(self, email):
        self.send_keys_to_field(PasswordPageLocators.email_input, email)

    @allure.step('Нажатие кнопки "Восстановить пароль"')
    def click_recovery_button(self):
        self.click_on_element(PasswordPageLocators.recover_button)

    @allure.step('Проверка наличия кнопки "Сохранить"')
    def check_save_button(self):
        return self.check_element(PasswordPageLocators.save_button)

    @allure.step('Проверка активности поля "Пароль"')
    def check_active_password_field(self, password):
        self.click_on_element(PasswordPageLocators.show_button)
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(PasswordPageLocators.password_input))
        password_field = self.driver.find_element(*PasswordPageLocators.password_input)
        password_field.send_keys(password)
        return password_field.get_attribute('value') == password

