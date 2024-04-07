import pytest
from page.LoginPage import LoginPage
from playwright.sync_api import Page

@pytest.fixture
def login_page(page: Page):
    return LoginPage(page)