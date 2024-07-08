import allure
import test_automation.utils.reporting as report
from test_automation.pages.sl_base import SLBasePage
from test_automation.pages.base_page import BasePage


class SLProductListPage(SLBasePage):

    def __init__(self, page):
        super().__init__(page)
        self.url = "/inventory.html"

        # Locators of common elements
        self.cart_link = self.page.locator("//a[@class='shopping_cart_link']")
        self.cart_count = self.page.locator("//span[@class='shopping_cart_badge']")
        self.sort_by_dropdown = self.page.locator("//select[@class='product_sort_container']")
        self.burger_menu = self.page.locator("//button[@id='react-burger-menu-btn']")
        self.about_link = self.page.locator("//a[@id='about_sidebar_link']")
        self.logout_link = self.page.locator("//a[@id='logout_sidebar_link']")
        self.all_items_link = self.page.locator("//a[@id='inventory_sidebar_link']")
        self.close_burger_menu_button = self.page.locator("//button[@id='react-burger-cross-btn']")

        # Locators of add to cart buttons of all products
        self.add_to_cart_backpack = self.page.locator("//button[@id='add-to-cart-sauce-labs-backpack']")
        self.add_to_cart_bikelight = self.page.locator("#add-to-cart-sauce-labs-bike-light")
        self.add_to_cart_bolt_tshirt = self.page.locator("//button[@id='add-to-cart-sauce-labs-bolt-t-shirt']")
        self.add_to_cart_fleece_jacket = self.page.locator("//button[@id='add-to-cart-sauce-labs-fleece-jacket']")
        self.add_to_cart_onesie = self.page.locator("//button[@id='add-to-cart-sauce-labs-onesie']")
        self.add_to_cart_test_all_things_tshirt = self.page.locator(
            "//button[@id='add-to-cart-test.allthethings()-t-shirt-(red)']")

    def open_burger_menu(self, **kwargs):
        self.burger_menu.click(**kwargs)

    def open_sort_by_dropdown(self):
        self.sort_by_dropdown.click()

    def logout(self, **kwargs):
        self.logout_link.click(**kwargs)

    def add_item_to_cart(self, product_name):
        self.page.locator(
            f"//*[text()='{product_name}']/ancestor::div[contains(@class,'inventory_item_label')]/following-sibling::div//button").click()

    def click_on_cart(self):
        self.cart_link.click()

    def go_to_product_list(self):
        self.open_burger_menu()
        self.all_items_link.click()

    def get_all_product_names(self):
        product_names_locators = self.page.query_selector_all("//a[contains(@data-test,'title-link')]")
        names=[]
        for p in product_names_locators:
            names.append(p.inner_text())
        print(names)
        return names

    def go_to_product_detail(self, product_name):
        self.page.locator(f"//*[text()='{product_name}']").click()

    def get_price_of_product(self, product_name):
        price = self.page.locator(f"//div[contains(@class, 'inventory_item_label')]//div[text()='{product_name}']/ancestor::div[contains(@class, 'inventory_item')]/following-sibling::div[contains(@class, 'pricebar')]//div[@data-test='inventory-item-price']").inner_text()
        return price