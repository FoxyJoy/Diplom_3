import allure
import pytest
from utils.urls import Urls
from pages.main_page import MainPage
from pages.profile_page import ProfilePage
from utils.data_generator import *

class TestMainPageBurgers:
    @allure.title('Переход на страницу конструктора при клике на «Конструктор»')
    def test_follow_to_constructor_page(self, driver):
        main_page = MainPage(driver)
        main_page.move_to_personal_account_button_and_click()
        main_page.click_constructor_button()
        assert main_page.check_constructor_form() and main_page.get_current_url() == Urls.url_main_page

    @allure.title('Переход на страницу ленты заказов при клике на «Лента заказов»')
    def test_follow_to_orders_feed_page(self, driver):
        main_page = MainPage(driver)
        main_page.move_to_personal_account_button_and_click()
        main_page.click_feed_button()
        assert main_page.check_orders_feed_form() and main_page.get_current_url() == Urls.url_order_feed_form

    @allure.title('При клике на ингредиент, появляется всплывающее окно с деталями')
    def test_check_bun_form(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_bun_button()
        assert main_page.check_bun_form()

    @allure.title('Закрытие всплывающего окна по клику на крестик')
    def test_close_fluorescent_bun_form(self, driver):
        main_page = MainPage(driver)
        main_page.click_on_bun_button()
        main_page.cloth_popup_form()
        assert main_page.check_close_popup_bun_form()

    @allure.title('Увеличение счетчика при добавлении ингредиента в заказ')
    def test_counter_ingredient(self, driver):
        main_page = MainPage(driver)
        main_page.add_bun()
        assert int(main_page.check_counter_ingredient()) > 0

    @allure.title('Оформление заказа залогиненным пользователем')
    def test_create_order(self, driver):
        email = generate_email()
        password = generate_password()
        name = generate_name()

        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        main_page.go_to_main_page()
        # нажать на кнопку личный кабинет
        profile_page.click_profile_cabinet_button()
        # нажать на текстовую ссылку - зарегистрироваться
        profile_page.click_registration_text_link()
        # ввести данные пользователя для регистрации
        # нажать на кнопку зарегистрироваться
        main_page.wait_registration_page()
        profile_page.enter_registration_data(name, email, password)
        # ввести данные пользователя для входа
        # нажать кнопку войти
        main_page.wait_login_page()
        profile_page.enter_login_data(email, password)
        main_page.click_constructor_button()
        main_page.create_order()
        assert main_page.check_order_form()



