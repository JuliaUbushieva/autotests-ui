from playwright.sync_api import sync_playwright, expect

with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False)
    page = browser.new_page()

    page.goto(
        'https://nikita-filonov.github.io/qa-automation-engineer-ui-course/#/auth/login',
        wait_until='networkidle'
    )

    # Trying to verify that a non-existent locator is visible on the page
    # unknown = page.locator('#unknown')
    # expect(unknown).to_be_visible()

    # Trying to enter text into the Login button
    # login_button = page.get_by_test_id('login-page-login-button')
    # login_button.fill('unknown')

    # Trying to change the header text
    page.evaluate(
        """
        const title = document.getElementById('authentication-ui-course-title-text')
        title.textContent = 'New Text'
        """
    )
