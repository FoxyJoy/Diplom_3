from selenium.webdriver.common.by import By

class LoginLocators:
    name_input = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    email_input = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    password_input = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    login_button = (By.XPATH, "//button[text()='Войти']")
    forgot_password_link = (By.XPATH, "//a[text()='Восстановить пароль']")
    register_button = (By.XPATH, "//button[text()='Зарегистрироваться']")
    place_an_order_button = (By.XPATH, "// button[text() = 'Оформить заказ']")
    register_text_link = (By.XPATH, "//a[@href='/register']")    # Кнопка "Зарегистрироваться"
    cabinet = (By.XPATH, "//p[text() = 'Личный Кабинет']")    #.//p[contains(text(), 'Личный Кабинет')]
    auth_form = (By.XPATH, ".//div[@class = 'Auth_login__3hAey']")    # Форма авторизации
    invisible_modal = (By.XPATH, "//div[@class ='Modal_modal_overlay__x2ZCr']")
    email_label = (By.XPATH, "//label[text()='Email']")
    password_label = (By.XPATH, "//label[text()='Пароль']")

class ProfilePageLocators:
    profile_button = (By.XPATH, ".//a[text() = 'Профиль']")   # Кнопка "Профиль" в Личном кабинете
    history_order_form = (By.XPATH, ".//div[@class = 'Account_contentBox__2CPm3']")   # Форма Истории заказов
    order_history_button = (By.XPATH, ".//a[text() = 'История заказов']")   # Кнопка "История заказов" в Личном кабинете
    exit_button = (By.XPATH, "//button[text()='Выход']")         # Кнопка "Выход" в Личном кабинете
    save_button = (By.XPATH, ".//button[text()='Сохранить']")  # Кнопка "Сохранить" в Личном кабинете
    profile_form = (By.XPATH, ".//div[@class = 'Account_account__vgk_w']")   # отображение формы личного кабинета

class MainPageLocators:
    constructor_button = (By.XPATH, ".//p[@class='AppHeader_header__linkText__3q_va ml-2'][text()='Конструктор']")    # (By.XPATH, ".//p[contains(text(), 'Конструктор')]")
    order_feed_button = (By.XPATH, ".//p[contains(text(), 'Лента Заказов')]")
    order_feed_link = (By.XPATH, ".//a[@class='AppHeader_header__link__3D_hX']")
    personal_account_button = (By.XPATH, ".//button[contains(text(), 'Войти в аккаунт')]")
    constructor_form = (By.XPATH, ".//div[@class = 'BurgerIngredients_ingredients__menuContainer__Xu3Mo']")
    fluorescent_bun_button = (By.XPATH, ".//img[@alt = 'Флюоресцентная булка R2-D3']")
    order_basket = (By.XPATH, ".//div[contains(@class, 'constructor-element_pos_top')]")
    order_feed_form = (By.XPATH, ".//div[@class = 'OrderFeed_orderFeed__2RO_j']")
    popup_form_ingredients = (By.XPATH, "//h2[text()= 'Детали ингредиента']")
    cloth_popup_form_button = (By.XPATH, ".//button[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    counter_ingredient = (By.XPATH, ".//p[contains(@class, 'counter_counter__num__3nue1')]")
    order_form = (By.XPATH, ".//div[@class = 'Modal_modal__container__Wo2l_']")
    place_order_button = (By.XPATH, ".//button[text() = 'Оформить заказ']")

class OrderFeedLocators:
    title_orders_list = (By.XPATH, '//h1[text()="Лента заказов"]')
    orders_info = (By.XPATH, '//p[text()="Cостав"]')
    total_orders_counter = (By.XPATH, "//p[text()='Выполнено за все время:']/following-sibling::p")
    daily_orders_counter = (By.XPATH, "//p[text()='Выполнено за сегодня:']/following-sibling::p")
    number_order_in_job = (By.XPATH, ".//li[contains(@class, 'text_type_digits-default')]")
    order_info_window = (By.XPATH, ".//li[contains(@class, 'OrderHistory_listItem__2x95r')][1]")
    order_history = (By.XPATH, './/p[contains(@class, "text_type_digits-default")]')
    target_drop_area = (By.XPATH, ".//ul[@class = 'BurgerConstructor_basket__list__l9dp_']")   # локатор области заказа
    target_in_order_feed = (By.XPATH, ".//ul[@class = 'OrderFeed_list__OLh59']")   #локатор заказов в ленте заказов
    number_of_created_order = (By.XPATH, ".//h2[@class = 'Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8']")

class PasswordPageLocators:
    email_input = (By.XPATH, ".//input[@name = 'name']")
    recover_button = (By.XPATH, ".//button[text() = 'Восстановить']")
    password_input = (By.XPATH, ".//input[@name = 'Введите новый пароль']")
    code_from_mail = (By.XPATH, ".//label[text() = 'Введите код из письма']")
    save_button = (By.XPATH, ".//button[text() = 'Сохранить']")
    recovery_text_form = (By.XPATH, ".//h2[text() = 'Восстановление пароля']")
    show_button = (By.XPATH, ".//div[@class = 'input__icon input__icon-action']")
    input_field_active = (By.CSS_SELECTOR, ".input.input_status_active")
    link_recovery_button = (By.XPATH, "//a[@href='/forgot-password']")

