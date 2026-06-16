from playwright.sync_api import Page, expect


class DashboardPage:
    """The dashboard the user lands on after a successful login."""

    def __init__(self, page: Page):
        self.page = page
        self.new_tasks_widget = page.get_by_text("New Tasks (24h)")

    def assert_loaded(self):
        expect(self.new_tasks_widget).to_be_visible()
