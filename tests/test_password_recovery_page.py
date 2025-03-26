import allure
import pytest
from utils.urls import Urls
from pages.main_page import MainPage
from pages.password_page import PasswordPage
from pages.profile_page import ProfilePage
from utils.data_generator import *

class TestPasswordPage:
    @allure.title('Переход на страницу восстановления пароля через кнопку "Восстановить пароль"')
    def test_follow_to_the_password_recovery_page(self, driver):
        profile_page = ProfilePage(driver)
        recovery_page = PasswordPage(driver)
        main_page = MainPage(driver)
        profile_page.go_to_main_page()
        main_page.move_to_personal_account_button_and_click()
        profile_page.click_recovery_button()
        assert recovery_page.check_recovery_form() and main_page.get_current_url() == Urls.url_password_forgot

    @allure.title('Ввод электронной почты и нажатие кнопки "Восстановить"')
    def test_input_password_and_click_recovery_btn(self, driver):
        profile_page = ProfilePage(driver)
        recovery_page = PasswordPage(driver)
        main_page = MainPage(driver)
        profile_page.go_to_main_page()
        main_page.move_to_personal_account_button_and_click()
        profile_page.click_recovery_button()
        recovery_page.input_email_to_email_field(generate_email())
        recovery_page.click_recovery_button()
        assert recovery_page.check_save_button() and main_page.get_current_url() == Urls.url_password_reset

    @allure.title('Проверка подсветки поля "Пароль"')
    def test_checking_the_backlight_of_the_password_field(self, driver):
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        recovery_page = PasswordPage(driver)
        main_page.move_to_personal_account_button_and_click()
        profile_page.click_recovery_button()
        recovery_page.input_email_to_email_field(generate_email())
        recovery_page.click_recovery_button()
        assert recovery_page.check_active_password_field(generate_password())
