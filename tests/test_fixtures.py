import pytest


@pytest.fixture(autouse=True)
def send_analytics_data():
    print("[AUTOUSE] Sent data to analytical service")


@pytest.fixture(scope="session")
def settings():
    print("[SESSION] Initiated autotests settings")


@pytest.fixture(scope="class")
def user():
    print("[CLASS] Created user data for one test class")


@pytest.fixture(scope="function")
def browser():
    print("[FUNCTION] Open browser for every test")


class TestUserFlow:
    def test_user_can_login(self, settings, user, browser):
        ...

    def test_user_can_create_course(self, settings, user, browser):
        ...


class TestAccountFlow:
    def test_user_account(self, settings, user, browser):
        ...
