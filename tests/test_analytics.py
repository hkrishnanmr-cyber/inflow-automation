import re
from playwright.sync_api import Page, expect

def test_page_elemets(page: Page) -> None:
    page.goto("https://qa.cirakas.com/analytics/")
    agree_btn = page.get_by_role("button",name="Accept")
    expect(agree_btn).to_be_visible()
    agree_btn.click()
    expect(page.get_by_role("heading", name="Application Analytics")).to_be_visible()
    expect(page.get_by_role("textbox", name="Search by name or project")).to_be_visible()
    expect(page.get_by_role("button", name="Last 30 Days")).to_be_visible()
    expect(page.get_by_role("combobox")).to_be_visible()
    expect(page.get_by_role("button", name="Export Team Performance")).to_be_visible()


def test_teamperformance_ColumnNames(page: Page) -> None:
    page.goto("https://qa.cirakas.com/analytics")
    page.wait_for_timeout(2000)
    # expect(page.get_by_role("cell", name="Team Member", exact=True).locator("span")).to_be_visible(timeout=10000)
    expect(page.get_by_text("Project Site", exact=True)).to_be_visible(timeout=10000)
    expect(page.get_by_text("Efficiency", exact=True)).to_be_visible()
    expect(page.get_by_text("Quality Score")).to_be_visible()
    expect(page.get_by_text("Workload")).to_be_visible()
    expect(page.get_by_text("Burnout Risk")).to_be_visible()
    expect(page.get_by_text("Avg Response Time")).to_be_visible()
    expect(page.get_by_text("Status")).to_be_visible()


def test_tabs_visibile(page: Page) -> None:
    page.goto("https://qa.cirakas.com/analytics")
    page.wait_for_timeout(2000)
    expect(page.get_by_role("tab", name="Team Performance")).to_be_visible(timeout=10000)
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

def test_taskdistribution_headers(page: Page) -> None:
    page.goto("https://qa.cirakas.com/analytics/")
    page.get_by_role("tab", name="Task Distribution").click()
    expect(page.get_by_text("Task Title")).to_be_visible()
    expect(page.get_by_text("Priority")).to_be_visible()
    expect(page.get_by_text("Status")).to_be_visible()
    expect(page.get_by_text("Project Site", exact=True)).to_be_visible()
    expect(page.get_by_text("Assigned To")).to_be_visible()
    expect(page.get_by_text("Due Date")).to_be_visible()
    expect(page.get_by_text("Complexity")).to_be_visible()
    print("All headers of task distribution are visible")



