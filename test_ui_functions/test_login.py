import time
import pytest

from playwright.sync_api import Playwright, sync_playwright


def test_login(set_up_login) -> None:
    page = set_up_login
    # Assess (Given)

    # browser = playwright.chromium.launch(headless=False, slow_mo=3000)
    # context = browser.new_context()
    # page = context.new_page()
    # page.goto("http://automationpractice.com/index.php")
    # #page.set_default_timeout(3000)

    # Login_Issue = True
    # while Login_Issue :
    #     if not page.is_visible("text='Sign in'"):
    #         page.click("text='Sign in'")
    #     else:
    #         Login_Issue = False

    # ACT  (When/And)
    # page.click("text=Sign in")
    # page.click("text='Sign in'")
    # page.click("input[name=\"email\"]")
    # page.fill("input[name=\"email\"]", "humblecat4real@yahoo.com")
    # # page.fill('input:below(:text("Email address"))', "humblecat4real@yahoo.com")
    # page.click("input[name=\"passwd\"]")
    # page.fill("input[name=\"passwd\"]", "Hunter")
    # page.click("button:has-text(\"Sign in\")")
    # # page.wait_for_load_state()
    # page.wait_for_selector("a:has-text(\"Hunter Doe\")")
    #
    # # Assert (Then)
    # time.sleep(3)
    # assert page.is_visible("text=Hunter Doe")

    # context.close()
    # browser.close()

# with sync_playwright() as playwright:
#     test_run(playwright)
