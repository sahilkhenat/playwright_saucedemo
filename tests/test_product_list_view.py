import allure
import pytest
import os
import test_automation.utils.data_generation as utils
import test_automation.utils.reporting as report
from test_automation.pages.sl_login import SLLoginPage
from test_automation.pages.sl_product_list_page import SLProductListPage
from test_automation.pages.sl_cart_page import SLCartPage


"""
Product list view related tests
"""


@allure.description("Verify that user is able to go to product list after login")
def test_go_to_product_list_(page):
    sl_product_list = SLProductListPage(page)
    sl_product_list.go_to_product_list()
    assert page.url == "https://www.saucedemo.com/inventory.html", report.report_fail(page,
                                                                                      "user is not navigated to expected url of product list view")


@allure.description("Verify that user is able to add an item to cart")
def test_add_an_item_to_cart(page, test_data):
    sl_product_list = SLProductListPage(page)
    sl_product_list.add_item_to_cart(test_data['product_name'])
    current_cart_count = sl_product_list.cart_count.inner_text()
    assert current_cart_count == "1"
    sl_cart = SLCartPage(page)
    assert sl_cart.is_product_in_cart(test_data['product_name']), report.report_fail(page,
                                                                                     f"{test_data['product_name']} not found in cart")


@allure.description("Verify that user is able to go to about link")
def test_go_to_about_section(page):
    sl_product_list = SLProductListPage(page)
    sl_product_list.open_burger_menu()
    sl_product_list.about_link.click()
    assert page.url == "https://saucelabs.com/", report.report_fail(page,
                                                                    "User is not navigated to expected about section URL")


@allure.description("Verify that user is able to logout from product list page")
def test_logout_from_product_list(page):
    sl_product_list = SLProductListPage(page)
    sl_product_list.open_burger_menu()
    sl_product_list.logout_link.click()
    assert page.url == "https://www.saucedemo.com/", report.report_fail(page, "User is not logged out as expected")


@allure.description("Verify that user is able to add an item to cart")
def test_remove_an_item_to_cart(page, test_data):
    sl_product_list = SLProductListPage(page)
    sl_product_list.add_item_to_cart(test_data['product_name'])
    sl_product_list.click_on_cart()
    sl_cart = SLCartPage(page)
    page.pause()
    sl_cart.remove_item_from_cart(test_data['product_name'])
    assert not sl_cart.is_product_in_cart(test_data['product_name']), report.report_fail(page, f"{test_data['product_name']} is still found in cart")
