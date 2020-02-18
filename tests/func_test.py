import os
from time import sleep

import pytest
from django.urls import reverse
from selenium.webdriver.firefox.webdriver import WebDriver


@pytest.fixture()
def home_page():
    return 'http://localhost:8000'


def test_start_page_with_files(browser: WebDriver, home_page):
    browser.get(home_page)
    assert browser.title == 'Feed files control - FFC'
    header_text = browser.find_element_by_tag_name('h1').text
    assert header_text == 'Feed files control - FFC'
    button = browser.find_element_by_id('id_new_manufacturers')
    button.click()
    form = browser.find_element_by_tag_name('form')
    assert form
    name_brand_field = browser.find_element_by_id('id_name_brand')
    file_field = browser.find_element_by_id("id_file_feed")
    name_brand_field.send_keys('Bosh')
    file_field.send_keys(os.path.join(os.path.dirname(__file__), "example.txt"))
    form.submit()
    sleep(3)
    table = browser.find_element_by_id('id_table_manufactured')
    rows = table.find_elements_by_tag_name('tr')
    assert any(row.text == 'Bosh' for row in rows)

