import pytest


@pytest.mark.parametrize("email, password", [("humblecat4real@yahoo.com", "Hunter"),
                                             pytest.param("humblecat4real@yahoo.com", " ", marks=pytest.mark.xfail)])
def test_parametrize(page, email, password):
    page.goto("http://automationpractice.com/index.php")
    # login_issue = True
    # while login_issue:
    #     if not page.is_visible("input[name=\"passwd\"]"):
    #         page.click("text='Sign in'")
    #     else:
    #         login_issue = False
    page.click("text=Sign in")
    page.click("input[name=\"email\"]")
    page.fill("input[name=\"email\"]", email)
    page.click("input[name=\"passwd\"]")
    page.fill("input[name=\"passwd\"]", password)
    page.click("button:has-text(\"Sign in\")")
