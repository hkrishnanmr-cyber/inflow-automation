import re
from playwright.sync_api import Page, expect

def test_teamperformance_ColumnNames(page: Page) -> None:
    page.goto("https://qa.cirakas.com/analytics")
    page.wait_for_timeout(2000)
    page.locator("div:nth-child(2) > .space-y-1 > a").first.click()
    expect(page.get_by_role("cell", name="Team Member", exact=True).locator("span")).to_be_visible()
    expect(page.get_by_text("Project Site", exact=True)).to_be_visible()
    expect(page.get_by_text("Efficiency", exact=True)).to_be_visible()
    expect(page.get_by_text("Quality Score")).to_be_visible()
    expect(page.get_by_text("Workload")).to_be_visible()
    expect(page.get_by_text("Burnout Risk")).to_be_visible()
    expect(page.get_by_text("Avg Response Time")).to_be_visible()
    expect(page.get_by_text("Status")).to_be_visible()
    expect(page.get_by_text("Action")).to_be_visible()


def test_element_visibile(page: Page) -> None:
    page.goto("https://qa.cirakas.com/dashboard")
    page.wait_for_timeout(2000)
    page.locator("div:nth-child(2) > .space-y-1 > a").first.click()
    expect(page.get_by_role("tab", name="Team Performance")).to_be_visible()
    expect(page.get_by_role("tab", name="Task Distribution")).to_be_visible()
    expect(page.get_by_role("tab", name="Project Site ROI")).to_be_visible()
    expect(page.get_by_role("tab", name="Application Health")).to_be_visible()
    expect(page.get_by_role("tab", name="Fund Analytics")).to_be_visible()
    expect(page.get_by_role("tab", name="Expense Analytics")).to_be_visible()
    expect(page.get_by_role("textbox", name="Search tasks...")).to_be_visible()
    expect(page.get_by_role("button", name="Last 30 Days")).to_be_visible()
    expect(page.get_by_role("combobox")).to_be_visible()
    expect(page.get_by_role("button", name="Export Task Distribution")).to_be_visible()
    expect(page.get_by_role("img").filter(has_text="May 18May 19May 20May 21May")).to_be_visible()



