# BEFORE
# import pytest
# from playwright.sync_api import sync_playwright, \
#     Page
#
#
# @pytest.fixture
# def chromium_page() -> Page:
#     with sync_playwright() as playwright:
#         browser = playwright.chromium.launch(headless=False)
#
#         yield browser.new_page()
#
#         browser.close()


# AFTER
import pytest
from playwright.sync_api import Playwright, Page


@pytest.fixture
def chromium_page(playwright: Playwright) -> Page:
    browser = playwright.chromium.launch(headless=False)
    yield browser.new_page()
    browser.close()
