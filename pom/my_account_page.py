import random
import string


class MyAccount:
    Order_History = "text=Order history and details"
    Credit_Slips = "text=My credit slips"
    Wishlists = "text=My wishlists"


class NewUser:
    def random_char(y):
        return "".join(random.choice(string.ascii_lowercase) for x in range(y))
    email_field = "input[name=\"email_create\"]"
    first_name_field = "input[name=\"customer_firstname\"]"
    last_name_field = "input[name=\"customer_lastname\"]"
    user_email = random_char(8)+"@yahoo.com"
    user_firstname = "Jane"
    user_last_name = "Doe"



