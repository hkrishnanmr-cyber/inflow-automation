from playwright.sync_api import Page


class LoginPage:
    """The Cirakas sign-in screen."""

    URL = "https://qa.cirakas.com/login"

    def __init__(self, page: Page):
        self.page = page
        self.email_input = page.get_by_role("textbox", name="Email")
        self.password_input = page.get_by_role("textbox", name="Password")
        self.sign_in_button = page.get_by_role("button", name="Sign In")

    def navigate(self):
        self.page.goto(self.URL)

    def login(self, email: str, password: str):
        self.email_input.click()
        self.email_input.fill(email)
        self.password_input.click()
        self.password_input.fill(password)
        self.sign_in_button.click()
