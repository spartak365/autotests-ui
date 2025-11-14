from playwright.sync_api import sync_playwright, expect
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list():

    # Запуск Playwright в синхронном режиме
    with sync_playwright() as playwright:
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

    # Создаем новую сессию с сохраненным состоянием
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        context = browser.new_context(storage_state="browser-state.json")  # Путь до файла с сохраненным состоянием
        page = context.new_page()

        page.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

        # Проверяем, что появился заголовок "Dashboard"
        courses_title = page.get_by_test_id("courses-list-toolbar-title-text")
        expect(courses_title).to_be_visible()
        expect(courses_title).to_have_text("Courses")

        # Проверяем, что появился заголовок "There is no results"
        there_is_no_result_title = page.get_by_test_id("courses-list-empty-view-title-text")
        expect(there_is_no_result_title).to_be_visible()
        expect(there_is_no_result_title).to_have_text("There is no results")

        # Проверяем, что появилась иконка пустого блока
        empty_block_icon = page.get_by_test_id("courses-list-empty-view-icon")
        expect(empty_block_icon).to_be_visible()

        # Проверяем, что появилось описание пустого блока "Results from the load test pipeline will be displayed here"
        empty_block_text = page.get_by_test_id("courses-list-empty-view-description-text")
        expect(empty_block_text).to_be_visible()
        expect(empty_block_text).to_have_text("Results from the load test pipeline will be displayed here")