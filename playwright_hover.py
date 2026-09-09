from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # Opening browser and creating a new page
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    # Going to the login page
    page.goto('https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login')

    registration_link = page.get_by_test_id('login-page-registration-link')
    registration_link.hover()

    page.wait_for_timeout(5000)