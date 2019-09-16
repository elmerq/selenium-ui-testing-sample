from time import sleep

from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

TEST_SITE='https://automationintesting.online/#/'

class WebTester():
    def __init__(self):
        # Create Browser
        opts = Options()
        
        self.browser = Firefox(opts)
        self.browser.get(TEST_SITE)

    def get_page_title(self):
        return (self.browser.title)

    def welcome_page_content(self):
        return self.browser.find_element_by_css_selector('.welcome .content')

    def welcome_next_page(self):
        self.browser.find_element_by_css_selector('#next').click()

    def welcome_modal_close(self):
        self.browser.find_element_by_css_selector('#closeModal').click()

    def book_this_room(self):
        self.browser.find_element_by_css_selector('.openBooking').click()

    def close_browser(self):
        self.browser.close()