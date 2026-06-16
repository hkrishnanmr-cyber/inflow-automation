import re

from playwright.sync_api import Page


class YopmailPage:
    """The Yopmail disposable inbox used to receive the verification code."""

    URL = "https://yopmail.com/"

    def __init__(self, page: Page):
        self.page = page
        self.login_input = page.get_by_role("textbox", name="Login")
        self.check_inbox_button = page.get_by_title("Check Inbox @yopmail.com")
        self.mail_frame = page.locator('iframe[name="ifmail"]').content_frame

    def navigate(self):
        self.page.goto(self.URL)

    def open_inbox(self, username: str):
        self.login_input.click()
        self.login_input.fill(username)
        self.check_inbox_button.click()

    def get_otp(self, attempts: int = 10, delay_ms: int = 3000) -> str:
        """Refresh the inbox until a 6-digit code appears, then return it.

        The email isn't always there the instant we look, so we re-check a
        few times before giving up.
        """
        for _ in range(attempts):
            self.check_inbox_button.click()          # refresh the inbox
            self.page.wait_for_timeout(delay_ms)     # let new mail land
            body = self.mail_frame.locator("body").inner_text()
            match = re.search(r"\d{6}", body)
            if match:
                return match.group()
        raise AssertionError("OTP email never arrived in the inbox")
