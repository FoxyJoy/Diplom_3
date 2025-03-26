## Дипломный проект. Задание 3: Веб-приложение

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающие классы `BurgersProfile`, `PasswordPage`, `OrderPageBurgers`, `MainPageBurgers`

Процент покрытия 100% (отчет: `htmlcov/index.html`)

---
### О репозитиории
#### В директории [utils](utils) лежат требуемые для тестов [Тестовые данные user-a](utils/data_generator.py) ,[urls](utils/urls.py).

#### В директории [pages](pages) лежат actions [для "Основного функционала"](pages/main_page.py), [для "Проверки заказов"](pages/order_page.py), [для "Проверки профииля"](pages/profile_page.py), [для "Проверки пароля"](pages/password_page.py), [для "Основного функционала"](pages/base_page.py)

#### В директории [locators](locators) лежат требуемые для тестов [Локаторы](locators/locators.py).

### Запуск автотестов

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск автотестов и создание HTML-отчета о покрытии**

>  `$ pytest --cov=praktikum --cov-report=html`








