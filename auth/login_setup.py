from playwright.sync_api import sync_playwright,expect
import re

AUTH_FILE = "auth/user.json"


def save_auth():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        name = "vivek"

        # LOGIN
        page.goto("https://qa.cirakas.com/login")
        page.get_by_role("textbox", name="Email").fill(f"{name}@yopmail.com")
        page.get_by_role("textbox",name="Password").fill("Cirakas@123456")
        page.get_by_role("button",name="Sign In").click()
        expect(page.get_by_text('OTP expires in:')).to_be_visible(timeout=10000)

        # OTP TAB
        otp_page = context.new_page()
        otp_page.goto("https://yopmail.com/")
        otp_page.get_by_role("textbox",name="Login").fill(name)
        otp_page.wait_for_timeout(5000)
        frame = otp_page.frame_locator('iframe[name="ifmail"]')
        otp = None
        for _ in range(10):
            otp_page.get_by_title("Check Inbox @yopmail.com").click()
            otp_page.wait_for_timeout(3000)
            body = frame.locator("body").inner_text()
            match = re.search(r"\d{6}",body)

            if match:
                otp = match.group()
                break

        assert otp
        otp_page.close()

        page.get_by_role("textbox", name="Verification Code").fill(otp)
        page.get_by_role("button",name="Verify").click()
        expect(page.get_by_role("button",name="Accept")).to_be_visible()
        page.get_by_role("button",name="Accept").click()
        

        # SAVE SESSION
        context.storage_state(path=AUTH_FILE)
        print("Auth saved")
        browser.close()

save_auth()