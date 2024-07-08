import allure
import pytest
import os
import test_automation.utils.data_generation as utils
import test_automation.utils.reporting as report
from test_automation.pages.sl_login import SLLoginPage
from test_automation.pages.sl_product_list_page import SLProductListPage


@allure.description("Verify that user is able to login with valid credentials")
def test_login_happy_flow(page):
    sl_login = SLLoginPage(page)
    sl_login.load()
    sl_login.login(os.getenv("USERNAME"), os.getenv("PASSWORD"))
    current_url = page.url
    assert current_url == "https://www.saucedemo.com/inventory.html", report.report_fail(page, "user did not navigate to product list page after login")


@allure.description("Verify that user is not able to login with invalid credentials")
def test_login_negative_flow(page):
    sl_login = SLLoginPage(page)
    sl_login.load()
    sl_login.login(os.getenv("INVALID_USERNAME"), os.getenv("PASSWORD"))
    login_error_message = sl_login.login_error.inner_text()
    assert login_error_message == "Epic sadface: Username and password do not match any user in this service", report.report_fail(page, "login error message is either incorrect or not displayed ")
    current_url = page.url
    assert current_url == "https://www.saucedemo.com/", report.report_fail(page, "user was navigated to product list page after login with invalid credentials")
