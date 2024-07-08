import os
import pytest
import test_automation.utils.data_generation as utils
from test_automation.pages.sl_login import SLLoginPage

"""Conftest file"""


@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "record_video_size": {
            "width": 1920,
            "height": 1080
        },
        "viewport": {
            "width": 1920,
            "height": 1080
        },
        "permissions": [
            "clipboard-read",
            "clipboard-write"
        ]
    }


@pytest.fixture(autouse=False)
def set_global_timeout(page) -> None:
    timeout = int(os.getenv("GLOBAL_TIMEOUT"))
    page.set_default_timeout(timeout)


@pytest.fixture(scope='session', autouse=True)
def get_credentials():
    d = dict()
    d['username'] = os.getenv("USERNAME")
    d['password'] = os.getenv("PASSWORD")
    return d


@pytest.fixture(autouse=True)
def login_to_sl(page):
    login_page = SLLoginPage(page)
    login_page.load()
    login_page.login(os.getenv("USERNAME"), os.getenv("PASSWORD"))


@pytest.fixture()
def test_data():
    dictionary = dict()
    dictionary['product_name'] = "Sauce Labs Backpack"
    return dictionary
