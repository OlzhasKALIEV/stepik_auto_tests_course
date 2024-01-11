import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


# Фикстуры в контексте PyTest — это вспомогательные функции для наших тестов, которые не являются частью тестового сценария.

@pytest.fixture(scope="class")
def browser():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()


class TestRegistration:
    def test_registration1(self, browser):
        browser.get("http://suninjuly.github.io/registration1.html")

        browser.find_element(By.CSS_SELECTOR, ".first_block .first").send_keys("John")
        browser.find_element(By.CSS_SELECTOR, ".first_block .second").send_keys("Doe")
        browser.find_element(By.CSS_SELECTOR, ".first_block .third").send_keys("john.doe@example.com")

        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        assert welcome_text == "Congratulations! You have successfully registered!"

    def test_registration2(self, browser):
        browser.get("http://suninjuly.github.io/registration2.html")

        browser.find_element(By.CSS_SELECTOR, ".form-control.first").send_keys("John")
        browser.find_element(By.CSS_SELECTOR, ".form-control.third").send_keys("Doe")
        browser.find_element(By.CSS_SELECTOR, ".form-control.first").send_keys("89026782409")
        browser.find_element(By.CSS_SELECTOR, ".form-control.econd").send_keys("89026782409")
        browser.find_element(By.CSS_SELECTOR, "button.btn").click()

        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        assert welcome_text == "Congratulations! You have successfully registered!"

