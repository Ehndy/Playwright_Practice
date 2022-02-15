import os

import pytest

try:
    PASSWORD = os.environ["PASSWORD"]
except KeyError:
    import utils.secret_config

    PASSWORD = utils.secret_config.PASSWORD


@pytest.fixture(scope="session")
def set_up(browser):
    # Assess (Given)

    # browser = playwright.chromium.launch(headless=False, slow_mo=3000)
    context = browser.new_context()
    page = context.new_page()
    page.goto("http://automationpractice.com/index.php")
    page.set_default_timeout(50000)

    yield page
    page.close()


@pytest.fixture(scope="session")
def set_up_login(set_up):
    page = set_up
    # login_issue = True
    # while login_issue:
    #     if not page.is_visible("input[name=\"passwd\"]"):
    #         page.click("text='Sign in'")
    #     else:
    #         login_issue = False
    page.click("text='Sign in'")
    page.click("input[name=\"email\"]")
    page.fill("input[name=\"email\"]", "humblecat4real@yahoo.com")
    page.click("input[name=\"passwd\"]")
    # page.fill("input[name=\"passwd\"]", utils.secret_config.PASSWORD)
    page.fill("input[name=\"passwd\"]", PASSWORD)
    page.click("button:has-text(\"Sign in\")")
    # assert page.is_visible("text=Hunter Doe")
