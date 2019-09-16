from time import sleep

import pytest
from selenium.common.exceptions import NoSuchElementException

from modal.webtester import WebTester

def test_page_modal():

    browser = WebTester()

    try:
        title = browser.get_page_title()
    except NoSuchElementException:
        pytest.fail(msg="Unable to find title of first page")

    assert "Restful-booker-platform demo" in title

    page_content = browser.welcome_page_content()

    assert "Welcome to Restful Booker Platform" in page_content.text

    browser.welcome_next_page()

    sleep(5)

    page_content = browser.welcome_page_content()

    print(page_content.text)

    sleep(5)

    browser.welcome_next_page()

    page_content = browser.welcome_page_content()

    print(page_content.text)

    sleep(5)

    browser.welcome_next_page()

    page_content = browser.welcome_page_content()

    print(page_content.text)

    sleep(5)

    browser.welcome_next_page()

    page_content = browser.welcome_page_content()

    print(page_content.text)

    sleep(5)

    browser.welcome_modal_close()

    sleep(5)

    browser.book_this_room()

    browser.close_browser()
