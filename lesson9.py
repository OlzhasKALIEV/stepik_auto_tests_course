import math

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


id_html = 'input_value'
x_path_html = '//*[@id="answer"]'

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")
    browser.execute_script("window.scrollBy(0, 100);")

    price_element = browser.find_element(By.ID, "price")
    wait = WebDriverWait(browser, 12)
    wait.until(EC.text_to_be_present_in_element((By.XPATH, '//*[@id="price"]'), "100"))
    button = browser.find_element(By.XPATH, '//*[@id="book"]')
    button.click()
    browser.execute_script("window.scrollBy(0, 600);")
    number = browser.find_element(By.ID, id_html)
    function_ur = calc(number.text)
    input1 = browser.find_element(By.XPATH, x_path_html)
    input1.send_keys(function_ur)
    button = browser.find_element(By.XPATH, '/html/body/form/div/div/button')
    button.click()
finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()