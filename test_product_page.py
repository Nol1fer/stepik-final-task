from time import sleep
import time

import pytest
from pages.basket_page import BasketPage
from pages.login_page import LoginPage
from pages.product_page import ProductPage


@pytest.mark.skip
@pytest.mark.parametrize(
    "link",
    [
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
        # "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
        pytest.param(
            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
            marks=pytest.mark.xfail,
        ),
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9",
    ],
)
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    # sleep(2)
    page.solve_quiz_and_get_code()
    # sleep(3)
    page.should_be_product_name_in_added_to_basket_message()
    # sleep(1)
    page.should_be_price_basket_equal_product_price()
    # sleep(2)


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    sleep(10)
    page.should_not_be_success_message()
    # sleep(5)


@pytest.mark.skip
def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


@pytest.mark.skip
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message_disappeared()


@pytest.mark.skip
def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.skip
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.skip
def test_guest_cant_see_product_in_basket_opened_from_main_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = ProductPage(browser, link)
    page.open()
    # go to basket page
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    # in basket should be no products
    basket_page.should_not_be_products_in_basket()
    # should be message that basket is empty
    basket_page.should_be_empty_basket_message()


class TestUserAddToBasketFromProductPage:
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        link = "https://selenium1py.pythonanywhere.com/en-gb/accounts/login/"
        page = LoginPage(browser, link)
        page.open()
        email = str(time.time()) + "@fakemail.org"
        password = "EB8mjx5F9QpM9FX"
        page.register_new_user(email, password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()

    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.add_product_to_basket()
        # sleep(2)
        # page.solve_quiz_and_get_code()
        # sleep(3)
        page.should_be_product_name_in_added_to_basket_message()
        # sleep(1)
        page.should_be_price_basket_equal_product_price()
        # sleep(2)
