import re
from playwright.sync_api import Page, expect


def test_login_random_mail(page: Page) -> None:
    page.goto("https://qa.cirakas.com/login")
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("hgdjhckj@errtf.bhn")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("cirakas@123456")
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Your account is not registered yet. Please sign up to create an account.")).to_be_visible()

def test_login_unregistered_user(page: Page) -> None:
    page.goto("https://qa.cirakas.com/login")
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("rajeev@yopail.com")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("cirakas@123456")
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Your account is not registered yet. Please sign up to create an account.")).to_be_visible()

def test_login_fail_wrong_pwd(page: Page) -> None:
    page.goto("https://qa.cirakas.com/login")
    page.get_by_role("textbox", name="Email").click()
    page.get_by_role("textbox", name="Email").fill("rajeev@yopmail.com")
    page.get_by_role("textbox", name="Password").click()
    page.get_by_role("textbox", name="Password").fill("cirakas@123456")
    page.get_by_role("button", name="Sign In").click()
    expect(page.get_by_text("Password is mismatch. Please enter the correct password.")).to_be_visible()


# def test_login(page: Page) -> None:
#     page.goto("https://qa.cirakas.com/login")
#     page.get_by_role("textbox", name="Email").click()
#     page.get_by_role("textbox", name="Email").fill("rajeev@yopmail.com")
#     page.get_by_role("textbox", name="Password").click()
#     page.get_by_role("textbox", name="Password").fill("Cirakas@123456")
#     page.get_by_role("button", name="Sign In").click()
#     page1 = page.context.new_page() # ← create the second tab
#     page1.goto("https://yopmail.com/")
#     page1.get_by_role("textbox", name="Login").click()
#     page1.get_by_role("textbox", name="Login").fill("rajeev")
#     page1.wait_for_timeout(5000)
#     # page1.get_by_title("Check Inbox @yopmail.com").click()
#     frame = page1.locator('iframe[name="ifmail"]').content_frame
#     otp = None
#     for _ in range(10):
#         page1.get_by_title("Check Inbox @yopmail.com").click()  # refresh the inbox
#         page1.wait_for_timeout(3000)                            # wait 3s for new mail
#         body = frame.locator("body").inner_text()
#         found = re.search(r"\d{6}", body)
#         if found:
#             otp = found.group()
#             break
#         assert otp, "OTP email never showed up"
#     print("OTP:", otp)
#     page.get_by_role("textbox", name="Verification Code").click()
#     page.get_by_role("textbox", name="Verification Code").fill(otp)
#     page.get_by_role("button", name="Verify").click()
#     page.get_by_role("button", name="Accept").click()
#     expect(page.get_by_text("New Tasks (24h)")).to_be_visible()
