from playwright.sync_api import Page


class VerificationPage:
    """The Cirakas verification-code screen shown after sign-in."""

    def __init__(self, page: Page):
        self.page = page
        self.code_input = page.get_by_role("textbox", name="Verification Code")
        self.verify_button = page.get_by_role("button", name="Verify")
        self.accept_button = page.get_by_role("button", name="Accept")

    def verify(self, otp: str):
        self.code_input.click()
        self.code_input.fill(otp)
        self.verify_button.click()
        self.accept_button.click()
