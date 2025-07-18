import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options



@pytest.fixture(scope="session")
def base_url():
    return "https://reqres.in/api"


@pytest.fixture(scope="session")
def api_session():
    session = requests.Session()
    session.headers.update({
        "x-api-key": "reqres-free-v1"
    })
    return session



@pytest.fixture(scope="function")
def driver():
    driver_path = r"C:\chromedriver-win64\chromedriver.exe" 
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    service = Service(driver_path)

    driver = webdriver.Chrome(service=service, options=chrome_options)
    yield driver
    driver.quit()