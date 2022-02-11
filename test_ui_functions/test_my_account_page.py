import time
import pytest

from pom.my_account_page import MyAccount

from playwright.sync_api import Playwright


def test_my_account(set_up) -> None:
    page = set_up
    # Assess (Given I launch browser Successfully)
    #
    # browser = playwright.chromium.launch(headless=False, slow_mo=1000)
    # context = browser.new_context()
    # page = context.new_page()
    # page.goto("http://automationpractice.com/index.php")
    # # page.set_default_timeout(3000)

    # Act (When I Log In)
    # page.click("text='Sign in'")

    # login_issue = True
    # while login_issue:
    #     if not page.is_visible("input[name=\"passwd\"]"):
    #         page.click("text='Sign in'")
    #     else:
    #         login_issue = False
    #
    # page.click("input[name=\"email\"]")
    # page.fill("input[name=\"email\"]", "humblecat4real@yahoo.com")
    # page.click("input[name=\"passwd\"]")
    # page.fill("input[name=\"passwd\"]", "Hunter")
    # page.click("button:has-text(\"Sign in\")")

    # page.wait_for_selector("text=Hunter Doe")
    # page.click("text=Hunter Doe")

    time.sleep(3)

    assert page.is_visible(MyAccount.Order_History)

    assert page.is_visible(MyAccount.Credit_Slips)

    assert page.is_visible(MyAccount.Order_History)

    # context.close()
    # browser.close()

# with sync_playwright() as playwright:
#     test_my_account(playwright)
