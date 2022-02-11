class Contact_Us_Page:
    def __init__(self, page):
        self.page = page

    def submit_form(self, email, message):
        self.page.click("text=Contact us")
        self.page.select_option("select[name=\"id_contact\"]", "2")
        self.page.fill("input[name=\"from\"]", email)
        self.page.fill("textarea[name=\"message\"]", message)
