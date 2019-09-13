from time import sleep
from webtester import WebTester

app_tester = WebTester()

sleep(5)

title = app_tester.get_page_title()

page_content = app_tester.welcome_page_content()

print(page_content.text)

app_tester.welcome_next_page()

sleep(5)

page_content = app_tester.welcome_page_content()

print(page_content.text)

sleep(5)

app_tester.welcome_next_page()

page_content = app_tester.welcome_page_content()

print(page_content.text)

sleep(5)

app_tester.welcome_next_page()

page_content = app_tester.welcome_page_content()

print(page_content.text)

sleep(5)

app_tester.welcome_next_page()

page_content = app_tester.welcome_page_content()

print(page_content.text)

sleep(5)

app_tester.welcome_modal_close()

sleep(5)

app_tester.book_this_room()

app_tester.close_browser()
