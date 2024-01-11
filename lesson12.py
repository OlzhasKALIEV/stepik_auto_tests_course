from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "https://stepik.org/lesson/236895/step/1"


value1 = '//*[@id="ember33"]'
value2 = '//*[@id="id_login_email"]'
value3 = '//*[@id="id_login_password"]'
value4= '//*[@id="ember100"]'
value5 = '//*[@id="ember78"]/div/section/div/div[1]/div[4]/button'

try:
    browser = webdriver.Chrome()
    browser.get(link)
    time.sleep(15)
    input1 = browser.find_element(By.XPATH, value1)
    input1.click()
    input2 = browser.find_element(By.XPATH, value2)
    input2.send_keys("kalievolzas8@gmail.com")
    input3 = browser.find_element(By.XPATH, value3)
    input3.send_keys("yyc66446deE")
    button = browser.find_element(By.XPATH, '//*[@id="login_form"]/button')
    button.click()
    time.sleep(10)
    input4 = browser.find_element(By.XPATH, value4)
    input4.send_keys(21.23)
    button = browser.find_element(By.XPATH, value5)
    button.click()
    time.sleep(10)

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()