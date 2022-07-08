import pytest
import json
from selene import browser


@pytest.fixture(scope='function', autouse=False)
def user_data():
    with open('../test_data/user.json') as user_file:
        data = json.load(user_file)
    return data


@pytest.fixture(scope='function', autouse=True)
def browser_quit():
    yield
    browser.quit()
