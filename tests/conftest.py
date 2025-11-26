import pytest
from playwright.sync_api import Playwright, Page, sync_playwright


@pytest.fixture(scope="session")
def initialize_browser_state(playwright: Playwright):
    # Открываем браузер Chromium
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()  # Создание контекста
    page = context.new_page()  # Создаем новую страницу

    # Переходим на страницу регистрации
    page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/registration")

    # Находим поле "Email" и заполняем его
    email_input = page.get_by_test_id("registration-form-email-input").locator('input')
    email_input.fill("user.name@gmail.com")

    # Находим поле "Username" и заполняем его
    username_input = page.get_by_test_id("registration-form-password-input").locator('input')
    username_input.fill("username")

    # Находим поле "Password" и заполняем его
    password_input = page.get_by_test_id("registration-form-password-input").locator('input')
    password_input.fill("password")

    # Находим кнопку "Registration" и кликаем на нее
    registration_button = page.get_by_test_id("registration-page-registration-button")
    registration_button.click()

    # Сохраняем данные контекста в JSON файл
    context.storage_state(path="browser-state.json")
    browser.close()


@pytest.fixture
def chromium_page_with_state(initialize_browser_state, playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context(storage_state="browser-state.json")  # Путь до файла с сохраненным состоянием
    yield context.new_page()
    browser.close()


@pytest.fixture
def chromium_page() -> Page:  # Аннотируем возвращаемое фикстурой значение
    # Ниже идет инициализация и открытие новой страницы
    with sync_playwright() as playwright:
        # Запускаем браузер
        browser = playwright.chromium.launch(headless=False)

        # Передаем страницу для использования в тесте
        yield browser.new_page()

        # Закрываем браузер после выполнения тестов
        browser.close()
