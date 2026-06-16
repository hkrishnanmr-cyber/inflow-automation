import re
from playwright.sync_api import Page, expect

word = "Test Playwright 2"


def test_task_creation(page: Page) -> None:
    page.goto("https://qa.cirakas.com/tasks")
    page.wait_for_timeout(2000)
    # word = "Test Playwright"

    # page.locator("a:nth-child(2)").first.click()
    page.get_by_role("button", name="+ Create Task").click()
    page.get_by_role("textbox", name="Title *").click()
    page.get_by_role("textbox", name="Title *").fill(word)
    page.get_by_role("textbox", name="Description *").click()
    page.get_by_role("textbox", name="Description *").fill(word)
    page.get_by_role("combobox").filter(has_text="Select priority").click()
    page.get_by_label("Urgent (Within 4 days)").get_by_text("Urgent (Within 4 days)").click()
    page.get_by_role("combobox").filter(has_text=re.compile(r"^Select project site$")).click()
    page.get_by_role("option", name="Kazhakootam").click()
    page.get_by_role("combobox", name="Type (Optional)").click()
    page.get_by_label("General").get_by_text("General").click()
    page.get_by_role("combobox").filter(has_text="Select staff member from").click()
    page.get_by_label("Vivek (Team Member)").get_by_text("Vivek (Team Member)").click()
    page.get_by_role("button", name="Create Task").click()
    page.get_by_role("textbox", name="Search by title, description").click()
    page.get_by_role("textbox", name="Search by title, description").fill("test")
    expect(page.get_by_text(word, exact=True).first).to_be_visible()


def test_task_search(page: Page) -> None:
    page.goto("https://qa.cirakas.com/tasks/")
    agree_btn = page.get_by_role("button",name="Accept")
    expect(agree_btn).to_be_visible()
    agree_btn.click()
    page.get_by_role('button', name= 'List' ).click()
    expect(page.get_by_text('Status')).to_be_visible(timeout=20000)
    word = "Test Playwright"
    page.get_by_role("textbox", name="Search by title, description").click()
    page.get_by_role("textbox", name="Search by title, description").fill(word)
    expect(page.get_by_text(word).first).to_be_visible()

import re
from playwright.sync_api import Page, expect


def test_task_edited(page: Page) -> None:
    page.goto("https://qa.cirakas.com/tasks/")
    agree_btn = page.get_by_role("button",name="Accept")
    expect(agree_btn).to_be_visible()
    agree_btn.click()
    page.get_by_role('button', name= 'List' ).click()
    expect(page.get_by_text('Status')).to_be_visible(timeout=20000)
    page.get_by_text(word).click()
    page.get_by_role("button", name="Edit").click()
    page.get_by_role("textbox", name="Title *").click()
    page.get_by_role("textbox", name="Title *").fill(f"{word} - edited")
    page.get_by_role("textbox", name="Description").click()
    page.get_by_role("textbox", name="Description").fill(f"{word} - edited")
    page.get_by_role("button", name="Update Task").click()
    page.get_by_role("button", name="Back").click()
    page.get_by_role("textbox", name="Search by title, description").click()
    page.get_by_role("textbox", name="Search by title, description").fill(f"{word} - edited")
    expect(page.get_by_text(f"{word} - edited")).to_be_visible()

