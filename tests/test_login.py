from playwright.sync_api import Page

from pages.login_page import LoginPage
from pages.yopmail_page import YopmailPage
from pages.verification_page import VerificationPage
from pages.dashboard_page import DashboardPage

# Move these to environment variables / a .env file before committing.
EMAIL = "rajeev@yopmail.com"
PASSWORD = "Cirakas@123456"
YOPMAIL_USER = "rajeev"


def test_login(page: Page) -> None:
    # 1. Sign in to the app
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(EMAIL, PASSWORD)

    # 2. Open a second tab and read the OTP from Yopmail
    mail_tab = page.context.new_page()
    yopmail = YopmailPage(mail_tab)
    yopmail.navigate()
    yopmail.open_inbox(YOPMAIL_USER)
    otp = yopmail.get_otp()
    print("OTP:", otp)
    mail_tab.close()

    # 3. Enter the code back in the app
    VerificationPage(page).verify(otp)

    # 4. Confirm we landed on the dashboard
    DashboardPage(page).assert_loaded()

def test_login_fail(page: Page) -> None:
    # 1. Sign in to the app
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login(EMAIL, "cirakas@123456")

    # 2. Open a second tab and read the OTP from Yopmail
    mail_tab = page.context.new_page()
    yopmail = YopmailPage(mail_tab)
    yopmail.navigate()
    yopmail.open_inbox(YOPMAIL_USER)
    otp = yopmail.get_otp()
    print("OTP:", otp)
    mail_tab.close()

    # 3. Enter the code back in the app
    VerificationPage(page).verify(otp)

    # 4. Confirm we landed on the dashboard
    DashboardPage(page).assert_loaded()
