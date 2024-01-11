import math

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture(scope="session")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()


@pytest.mark.parametrize('links', ['https://stepik.org/lesson/236895/step/1',
                                   'https://stepik.org/lesson/236896/step/1',
                                   'https://stepik.org/lesson/236897/step/1',
                                   'https://stepik.org/lesson/236898/step/1',
                                   'https://stepik.org/lesson/236899/step/1',
                                   'https://stepik.org/lesson/236903/step/1',
                                   'https://stepik.org/lesson/236904/step/1',
                                   'https://stepik.org/lesson/236905/step/1'])
def test_stepik_login(browser, links):
    value1 = '//*[@id="ember33"]'
    value2 = '//*[@id="id_login_email"]'
    value3 = '//*[@id="id_login_password"]'
    browser.get(links)

    try:
        time.sleep(15)
        input1 = browser.find_element(By.XPATH, value1)
        input1.click()

        input2 = browser.find_element(By.XPATH, value2)
        input2.send_keys("kalievolzas8@gmail.com")

        input3 = browser.find_element(By.XPATH, value3)
        input3.send_keys("yyc66446deE")
        button_element = browser.find_element(By.XPATH, '//*[@id="login_form"]/button')
        button_element.click()
        time.sleep(15)
        button = browser.find_element(By.CLASS_NAME, 'again-btn')
        button.click()
        text = browser.find_element(By.CLASS_NAME, 'ember-text-area')
        answer = math.log(int(time.time()))
        text.send_keys(answer)
        button = browser.find_element(By.CLASS_NAME, 'submit-submission')
        button.click()
    except NoSuchElementException:
        print("Кнопка 'Решить снова' не найдена")
    finally:
        time.sleep(10)
        text = browser.find_element(By.CLASS_NAME, 'ember-text-area')
        answer = math.log(int(time.time()))
        text.send_keys(answer)
        time.sleep(5)
        button = browser.find_element(By.CLASS_NAME, 'submit-submission')
        button.click()
        time.sleep(10)
        button = browser.find_element(By.CLASS_NAME, 'again-btn')
        button.click()
