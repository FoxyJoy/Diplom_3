import allure
import pytest
from pages.profile_page import ProfilePage
from utils.urls import Urls
from utils.data_generator import *

class TestBurgersProfile:
    @allure.title('переход по клику на «Личный кабинет»')
    def test_go_to_profile(self, driver):
        email = generate_email()
        password = generate_password()
        name = generate_name()

        profile_page = ProfilePage(driver)
        # зайти на сайт
        profile_page.go_to_main_page()
        # нажать на кнопку личный кабинет
        profile_page.click_profile_cabinet_button()
        # нажать на текстовую ссылку - зарегистрироваться
        profile_page.click_registration_text_link()
        # ввести данные пользователя для регистрации
        # нажать на кнопку зарегистрироваться
        profile_page.wait_registration_page()
        profile_page.enter_registration_data(name, email, password)
        # ввести данные пользователя для входа
        # нажать кнопку войти
        profile_page.wait_login_page()
        profile_page.enter_login_data(email, password)
        # нажать на кнопку личный кабинет
        profile_page.click_profile_cabinet_button()
        # проверить то что появился текст "История заказов"
        assert Urls.url_order_history

    @allure.title('переход в раздел «История заказов»')
    def test_go_to_order_history(self, driver):
        email = generate_email()
        password = generate_password()
        name = generate_name()

        profile_page = ProfilePage(driver)
        profile_page.go_to_main_page()
        # нажать на кнопку личный кабинет
        profile_page.click_profile_cabinet_button()
        # нажать на текстовую ссылку - зарегистрироваться
        profile_page.click_registration_text_link()
        # ввести данные пользователя для регистрации
        # нажать на кнопку зарегистрироваться
        profile_page.wait_registration_page()
        profile_page.enter_registration_data(name, email, password)
        profile_page.wait_login_page()
        profile_page.enter_login_data(email, password)
        profile_page.click_profile_cabinet_button()
        # нажать на кнопку "История заказов"
        profile_page.click_history_orders_button()
        assert profile_page.check_profile_area_form() and profile_page.get_current_url() == Urls.url_order_history

    @allure.title('Выход из аккаунта')
    def test_logout_from_account(self, driver):
        email = generate_email()
        password = generate_password()
        name = generate_name()

        profile_page = ProfilePage(driver)
        profile_page.go_to_main_page()
        # нажать на кнопку личный кабинет
        profile_page.click_profile_cabinet_button()
        # нажать на текстовую ссылку - зарегистрироваться
        profile_page.click_registration_text_link()
        # ввести данные пользователя для регистрации
        # нажать на кнопку зарегистрироваться
        profile_page.wait_registration_page()
        profile_page.enter_registration_data(name, email, password)
        profile_page.wait_login_page()
        profile_page.enter_login_data(email, password)
        profile_page.click_profile_cabinet_button()
        # нажать на кнопку "Выход"
        profile_page.click_exit_button()
        assert profile_page.check_authorization_form() and profile_page.get_current_url() == Urls.url_login_form
