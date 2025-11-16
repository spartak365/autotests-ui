from playwright.sync_api import Playwright, expect, Page
import pytest


@pytest.mark.courses
@pytest.mark.regression
def test_empty_courses_list(chromium_page_with_state: Page):

    chromium_page_with_state.goto("https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/courses")

    # Проверяем, что появился заголовок "Dashboard"
    courses_title = chromium_page_with_state.get_by_test_id("courses-list-toolbar-title-text")
    expect(courses_title).to_be_visible()
    expect(courses_title).to_have_text("Courses")

    # Проверяем, что появился заголовок "There is no results"
    there_is_no_result_title = chromium_page_with_state.get_by_test_id("courses-list-empty-view-title-text")
    expect(there_is_no_result_title).to_be_visible()
    expect(there_is_no_result_title).to_have_text("There is no results")

    # Проверяем, что появилась иконка пустого блока
    empty_block_icon = chromium_page_with_state.get_by_test_id("courses-list-empty-view-icon")
    expect(empty_block_icon).to_be_visible()

    # Проверяем, что появилось описание пустого блока "Results from the load test pipeline will be displayed here"
    empty_block_text = chromium_page_with_state.get_by_test_id("courses-list-empty-view-description-text")
    expect(empty_block_text).to_be_visible()
    expect(empty_block_text).to_have_text("Results from the load test pipeline will be displayed here")