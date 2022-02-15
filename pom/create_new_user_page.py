import time
from pom.my_account_page import NewUser


class Create_new_user:
    def __init__(self, page):
        self.page = page

    def fill_new_user_form(self, ):
        self.page.click("text=Sign in")
        self.page.fill(NewUser.email_field, NewUser.user_email)

        with self.page.expect_navigation():
            self.page.click("button:has-text(\"Create an account\")")

            time.sleep(5)

        self.page.click("input[name=\"id_gender\"]")

        self.page.fill(NewUser.first_name_field, NewUser.user_firstname)
        self.page.fill(NewUser.last_name_field, NewUser.user_last_name)
        self.page.fill("input[name=\"passwd\"]", "Hunter")
        self.page.select_option("select[name=\"days\"]", "26")
        self.page.select_option("select[name=\"months\"]", "12")
        self.page.select_option("select[name=\"years\"]", "1993")
        self.page.fill("input[name=\"firstname\"]", "Jane")
        self.page.fill("input[name=\"lastname\"]", "Doe")
        self.page.fill("input[name=\"address1\"]", "123 test ave")
        self.page.fill("input[name=\"city\"]", "New york")
        self.page.select_option("select[name=\"id_state\"]", "32")
        self.page.click("input[name=\"postcode\"]")
        self.page.fill("input[name=\"postcode\"]", "00000")
        self.page.fill("input[name=\"phone\"]", "0987654321")
        self.page.fill("input[name=\"phone_mobile\"]", "0987654321")
        time.sleep(3)
        self.page.click("button:has-text(\"Register\")")
        time.sleep(5)

        assert self.page.is_visible("text=Jane Doe", timeout=10000)
