from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class GooglePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.google.com"
        self.search_box = (By.NAME, "q")

    def open(self):
        self.driver.get(self.url)
        try:
            # Приема бисквитки, ако бутонът се появи
            consent_button = WebDriverWait(self.driver, 5).until(
                EC.element_to_be_clickable((By.ID, "L2AGLb"))
            )
            consent_button.click()
        except:
            pass  # ако не се появи, продължаваме

    def search(self, text):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.search_box)
        ).send_keys(text + "\n")