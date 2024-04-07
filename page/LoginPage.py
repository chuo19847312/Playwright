from playwright.sync_api import expect

class LoginPage:
    def __init__(self, page):
        self.page = page
        self.base_url = "https://www.saucedemo.com"

    def navigate(self):
        self.page.goto(self.base_url)

    def login_account(self, username: str, password: str):
        self.page.locator("//input[@placeholder='Username']").fill(username)
        self.page.locator("//input[@placeholder='Password']").fill(password)
        self.page.locator("//input[@name='login-button']").click()
    
    def visitInventoryPage(self):
        self.page.goto(self.base_url+"/inventory.html")

    def clickElementByXpath(self, xpath: str):
        self.page.locator(xpath).click()

    def clickAbout(self):
        self.clickElementByXpath("//button[contains(text(), 'Open Menu')]")
        self.clickElementByXpath("//a[contains(text(), 'About')]")

    def shouldDisplayTitle(self):
        expect(self.page.locator("//div[contains(text(), 'Swag Labs')]")).to_be_visible()

    def shouldDisplayErrorWithProblemUser(self):
        expect(self.page.locator("//h2[contains(text(), 'Uh oh! This page got lost in the web.')]")).to_be_visible()

    def shouldDisplayErrorWithoutLogin(self):
        expect(self.page.locator('//h3[contains(text(),"Epic sadface: You can only access \'/inventory.html\' when you are logged in.")]')).to_be_visible()

    def shouldDisplayLockoutMessage(self):
        expect(self.page.locator("h3")).to_have_text("Epic sadface: Sorry, this user has been locked out.")
    
