import os
import pytest
from playwright.sync_api import sync_playwright
from auth.login_setup import save_auth

AUTH_FILE = "auth/user.json"


@pytest.fixture(scope="session")
def page():

    # Create auth if missing
    if not os.path.exists(AUTH_FILE):
        save_auth()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(storage_state=AUTH_FILE)
        page = context.new_page()
        yield page

        context.close()
        browser.close()