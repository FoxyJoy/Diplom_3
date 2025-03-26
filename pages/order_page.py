import allure
from pages.base_page import BasePage
from locators.locators import *

class OrderFeedPage(BasePage):
    @allure.step('Клик по первому заказу в списке "Лента заказов"')
    def click_order_info(self):
        self.click_on_element(OrderFeedLocators.order_info_window)

    @allure.step('Проверка видимости формы заказа')
    def check_order_info_modal(self):
        return self.check_element(OrderFeedLocators.orders_info)

    @allure.step('Получение заказов со статусом "В работе"')
    def get_orders_in_progress(self):
        elements = self.get_text_locators(OrderFeedLocators.number_order_in_job)
        orders_list = []
        for element in elements:
            order_number = element.text[1:]
            orders_list.append(order_number)
        return orders_list

    @allure.step('Получение номеров заказов')
    def get_orders_history(self):
        elements = self.get_text_locators(OrderFeedLocators.order_history)
        orders_list = []
        for element in elements:
            order_number = element.text[2:]
            orders_list.append(order_number)
        return orders_list

    @allure.step('Используем WebDriverWait для ожидания появления номера заказа')
    def get_created_order_number(self):
        self.wait_text(OrderFeedLocators.number_of_created_order, OrderFeedLocators.number_of_created_order_text)
        return self.get_text_locator(OrderFeedLocators.number_of_created_order)

    @allure.step('Получение количества заказов')
    def check_counter_orders(self, locator):
        counter_text = self.get_text_locator(locator)
        return int(counter_text)  # Преобразуем текст в число
