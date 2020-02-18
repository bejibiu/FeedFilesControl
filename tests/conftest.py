import pytest
from selenium import webdriver


@pytest.fixture(scope="class")
def browser(request):
    ff_driver = webdriver.Firefox()
    yield ff_driver
    ff_driver.close()
