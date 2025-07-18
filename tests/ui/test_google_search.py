from tests.ui.pages.google_page import GooglePage

def test_google_search(driver):
    google = GooglePage(driver)
    google.open()
    google.search("OpenAI ChatGPT")

    assert "OpenAI" in driver.title