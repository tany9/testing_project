from pages.login_page import LoginPage

def test_user_can_login(driver):
    login_page = LoginPage(driver)  # Виж, тук е с главна буква
    login_page.open()
    login_page.enter_username("Admin")
    login_page.enter_password("admin123")
    login_page.click_login()

    assert "dashboard" in driver.current_url