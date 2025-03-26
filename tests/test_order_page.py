import allure
import pytest
from pages.main_page import MainPage
from pages.order_page import OrderFeedPage
from pages.profile_page import ProfilePage
from locators.locators import *
from utils.data_generator import *

class TestOrderPageBurgers:
    @allure.title('Проверка модального окна с деталями заказа')
    def test_check_order_info_modal(self, driver):
        main_page = MainPage(driver)
        main_page.click_feed_button()
        order_page = OrderFeedPage(driver)
        order_page.click_order_info()
        assert order_page.check_order_info_modal()

    @allure.title('Проверка появления заказа в Ленте заказов')
    def test_check_user_orders_in_orders_history(self, driver):
        email = generate_email()
        password = generate_password()
        name = generate_name()

        main_page = MainPage(driver)
        order_page = OrderFeedPage(driver)
        profile_page = ProfilePage(driver)
        # нажать на кнопку личный кабинет
        profile_page.click_profile_cabinet_button()
        # нажать на текстовую ссылку - зарегистрироваться
        profile_page.click_registration_text_link()
        # ввести данные пользователя для регистрации
        # нажать на кнопку зарегистрироваться
        main_page.wait_registration_page()
        profile_page.enter_registration_data(name, email, password)
        # нажать кнопку войти
        main_page.wait_login_page()
        profile_page.enter_login_data(email, password)
        # Клик на конструктор после регистрации
        main_page.click_constructor_button()
        # Добавление ингредиентов в заказ с помощью перетаскивания
        main_page.drag_and_drop(MainPageLocators.fluorescent_bun_button, OrderFeedLocators.target_drop_area)
        # Нажать на кнопку "Оформить заказ"
        main_page.click_place_order_button()
        # Ожидание появления номера заказа
        order_number = order_page.get_created_order_number()
        main_page.cloth_popup_form()
        # Переход в ленту заказов
        main_page.click_feed_button()
        # Проверка, что заказ появился в ленте заказов
        orders_in_feed = order_page.get_orders_history()
        assert order_number in orders_in_feed

    @allure.title('при создании нового заказа счётчик Выполнено за всё время увеличивается')
    @pytest.mark.parametrize('counter', [OrderFeedLocators.daily_orders_counter, OrderFeedLocators.total_orders_counter])
    def test_update_counter_orders(self, driver, counter):
        email = generate_email()
        password = generate_password()
        name = generate_name()

        order_page = OrderFeedPage(driver)
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        # нажать на кнопку личный кабинет
        profile_page.click_profile_cabinet_button()
        # нажать на текстовую ссылку - зарегистрироваться
        profile_page.click_registration_text_link()
        # ввести данные пользователя для регистрации
        # нажать на кнопку зарегистрироваться
        main_page.wait_registration_page()
        profile_page.enter_registration_data(name, email, password)
        # Нажать кнопку "Войти"
        main_page.wait_login_page()
        profile_page.enter_login_data(email, password)
        # Переход в ленту заказов
        main_page.click_feed_button()
        # Получение текущего значения счетчика
        actual_counter = int(order_page.check_counter_orders(counter))
        # Переход в конструктор
        main_page.click_constructor_button()
        # # Добавление ингредиентов в заказ с помощью перетаскивания
        main_page.drag_and_drop(MainPageLocators.fluorescent_bun_button, OrderFeedLocators.target_drop_area)
        # # Нажать на кнопку "Оформить заказ"
        main_page.click_place_order_button()
        # # Ожидание появления номера заказа
        order_page.get_created_order_number()
        # Закрытие всплывающего окна
        main_page.cloth_popup_form()
        # Переход в ленту заказов
        main_page.click_feed_button()
        # Получение нового значения счетчика
        new_counter = int(order_page.check_counter_orders(counter))
        assert new_counter > actual_counter

    @allure.title('Проверка смены Статуса заказа')
    def test_check_user_order_in_progress(self, driver):
        email = generate_email()
        password = generate_password()
        name = generate_name()

        order_page = OrderFeedPage(driver)
        main_page = MainPage(driver)
        profile_page = ProfilePage(driver)
        profile_page.click_profile_cabinet_button()
        profile_page.click_registration_text_link()
        main_page.wait_registration_page()
        profile_page.enter_registration_data(name, email, password)
        main_page.wait_login_page()
        profile_page.enter_login_data(email, password)
        main_page.click_constructor_button()
        main_page.drag_and_drop(MainPageLocators.fluorescent_bun_button, OrderFeedLocators.target_drop_area)
        main_page.click_place_order_button()
        new_order = order_page.get_created_order_number()
        main_page.cloth_popup_form()
        main_page.click_feed_button()
        user_order = order_page.get_orders_in_progress()
        assert new_order in user_order