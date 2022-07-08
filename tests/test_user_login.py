from pages import login_page


def test_user_login(user_data):
    login_page.load()
    login_page.switch_to_login()
    login_page.type_email(user_data['email']) \
        .type_password(user_data['password'])
    login_page.click_on_login_button()
    login_page.wait_till_main_page_loaded()
    assert login_page.username_is(user_data['full_username'])
