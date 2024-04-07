from page.LoginPage import LoginPage
from playwright.sync_api import Page


class TestSauceDemoLogin:
    def test_01_signInStandardUser(page: Page, login_page:LoginPage):
        login_page.navigate()
        login_page.login_account('standard_user', 'secret_sauce')
        login_page.shouldDisplayTitle()
    
    def test_02_lockOutUser(page: Page, login_page: LoginPage):
        login_page.navigate()
        login_page.login_account('locked_out_user', 'secret_sauce')
        login_page.shouldDisplayLockoutMessage()

    def test_03_problemUser(page: Page, login_page: LoginPage):
        login_page.navigate()
        login_page.login_account('problem_user', 'secret_sauce')
        login_page.clickAbout()
        login_page.shouldDisplayErrorWithProblemUser()

    def test_04_checkInventoryWithoutLogin(page: Page, login_page: LoginPage):
        login_page.visitInventoryPage()
        login_page.shouldDisplayErrorWithoutLogin()
