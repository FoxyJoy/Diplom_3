import time

import allure
from pages.base_page import BasePage
from locators.locators import *

class MainPage(BasePage):
    @allure.step('Прокрутка к кнопке "Войти в аккаунт" и нажатие на нее')
    def move_to_personal_account_button_and_click(self):
        self.move_to_element_and_click(MainPageLocators.personal_account_button)

    @allure.step('Нажать на кнопку "Конструктор"')
    def click_constructor_button(self):
        self.move_to_element_and_click(MainPageLocators.constructor_button)

    @allure.step('Проверка формы конструктора')
    def check_constructor_form(self):
        return self.check_element(MainPageLocators.constructor_form)

    @allure.step('Нажать на кнопку "Лента заказов"')
    def click_feed_button(self):
        self.move_to_element_and_click(MainPageLocators.order_feed_link)

    @allure.step('Проверка формы ленты заказов')
    def check_orders_feed_form(self):
        return self.check_element(MainPageLocators.order_feed_form)

    @allure.step('Нажать на кнопку "Личный кабинет"')
    def click_profile_area_button(self):
        self.move_to_element_and_click(MainPageLocators.personal_account_button)

    @allure.step('Нажатие на кнопку "Булки"')
    def click_on_bun_button(self):
        self.move_to_element_and_click(MainPageLocators.fluorescent_bun_button)

    @allure.step('Закрыть форму конструктора булки')
    def cloth_popup_form(self):
        self.click_on_element(MainPageLocators.cloth_popup_form_button)

    @allure.step('Проверка закрытия формы "Информация о булке"')
    def check_close_popup_bun_form(self):
        return self.check_element_is_not_visible(MainPageLocators.popup_form_ingredients)

    @allure.step('Получение значения счетчика ингредиента')
    def check_counter_ingredient(self):
        return self.get_text_locator(MainPageLocators.counter_ingredient)

    @allure.step('Добавление булки в корзину')
    def add_bun(self):
        self.drag_and_drop(MainPageLocators.fluorescent_bun_button, MainPageLocators.order_basket)

    @allure.step('Нажатие на кнопку "Оформить заказ"')
    def click_place_order_button(self):
        self.click_on_element(MainPageLocators.place_order_button)

    @allure.step('Создание заказа')
    def create_order(self):
        self.add_bun()
        self.click_place_order_button()

    @allure.step('Проверка отображения формы "Оформление заказа"')
    def check_order_form(self):
        return self.check_element(MainPageLocators.order_form)


    @allure.step('Проверка формы "Детали ингредиента"')
    def check_bun_form(self):
        return self.check_element(MainPageLocators.popup_form_ingredients)






