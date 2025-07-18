from selenium.webdriver.common.by import By

class LoginPageLocators:
    USERNAME_INPUT = (By.NAME, "username")
    PASSWORD_INPUT = (By.NAME, "password")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

class HomePageLocators:
    DASHBOARD_TITLE = (By.CSS_SELECTOR, ".oxd-topbar-header-title")