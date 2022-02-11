from playwright.sync_api import Playwright, sync_playwright
from pom.contact_us_page import Contact_Us_Page
import pytest



def test_contact_us(playwright: Playwright):
    # Assess (Given I launch browser Successfully)

    browser = playwright.chromium.launch(headless=False, slow_mo=3000)
    page = browser.new_page()
    contact_us = Contact_Us_Page(page)
    contact_us.navigate()
    contact_us.submit_form("humblecat4real@yahoo.com", "This is the message")


# with sync_playwright() as playwright:
#     test_contact_us(playwright)
