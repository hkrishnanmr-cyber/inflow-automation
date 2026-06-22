import re
from playwright.sync_api import Page, expect


# def test_fund_creation(page: Page) -> None:
#     page.goto("https://qa.cirakas.com/petty-cash/")
#     agree_btn = page.get_by_role("button",name="Accept")
#     expect(agree_btn).to_be_visible()
#     agree_btn.click()
#     fund_name = "Test fund 2"
#     amount = 1000
#     page.get_by_role("button", name="Create Fund").click()
#     page.get_by_role("textbox", name="Fund Name").fill(fund_name)
#     page.get_by_role("combobox").click()
#     page.get_by_role("option", name="Menamkulam").click()
#     page.get_by_role("spinbutton", name="Initial Amount").click()
#     page.get_by_role("spinbutton", name="Initial Amount").fill(str(amount))
#     page.get_by_role("spinbutton", name="Low Balance Threshold").click()
#     page.get_by_role("spinbutton", name="Low Balance Threshold").fill("10")
#     page.get_by_role("textbox", name="Notes").click()
#     page.get_by_role("textbox", name="Notes").fill("Test note")
#     page.get_by_role("button", name="Create Fund").click()
#     page.get_by_role("textbox", name="Search funds...").click()
#     page.get_by_role("textbox", name="Search funds...").fill(fund_name)
#     expect(page.get_by_text(fund_name).first).to_be_visible()


def test_recharged_fund_in_FundAnalytics(page: Page) -> None:
    fund_name = "Test fund 2"
    recharge_amount = 10
    page.goto("https://qa.cirakas.com/petty-cash/")
    page.get_by_role("textbox", name="Search funds...").click()
    page.get_by_role("textbox", name="Search funds...").fill(fund_name)
    page.get_by_role("button", name="Recharge Fund").first.click()
    page.get_by_role("textbox", name="Amount to Add *").fill(str(recharge_amount))
    page.get_by_role("textbox", name="Notes (Optional)").click()
    page.get_by_role("textbox", name="Notes (Optional)").fill("test note")
    page.get_by_role("button", name="Recharge").click()
    expect(page.get_by_text("1020.00").first).to_be_visible()
    page.locator("div:nth-child(2) > .space-y-1 > a").first.click()
    page.get_by_role("tab", name="Fund Analytics").click()
    page.get_by_role("textbox", name="Search funds...").click()
    page.get_by_role("textbox", name="Search funds...").fill(fund_name)
    expect(page.get_by_role("cell", name=fund_name).first).to_be_visible()
    expect(page.get_by_text("Recharge")).to_be_visible()
    expect(page.locator("tbody")).to_contain_text(f"₹{recharge_amount}.00")

