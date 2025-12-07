import pytest

from utils import driver_factory
from utils.driver_factory import create_driver


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help='use chrome or firefox or edge')


@pytest.fixture
def driver(request):
    browser = request.config.getoption("--browser")
    driver = create_driver(browser)
    yield driver
    driver.quit()

