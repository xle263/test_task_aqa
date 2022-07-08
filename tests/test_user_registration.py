from time import sleep
from pages import login_page


def test_register_new_user(user_data):
    login_page.load()
    login_page.type_email(user_data['email'])\
        .type_first_name(user_data['first_name'])\
        .type_last_name(user_data['last_name'])\
        .type_password(user_data['password'])
    login_page.submit_privacy_agreement()
    sleep(5)
    login_page.click_on_registration_button()
    login_page.check_confirm_registration_page_loaded()
