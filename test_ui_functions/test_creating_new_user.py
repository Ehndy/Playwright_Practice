from pom.create_new_user_page import Create_new_user
from pom.my_account_page import NewUser


def test_creating_new_user(set_up):
    page = set_up

    new_user = Create_new_user(page)
    new_user.fill_new_user_form()
