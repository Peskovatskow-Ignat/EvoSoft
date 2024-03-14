import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from time import sleep
from random import randint


options = Options()
driver = webdriver.Chrome(options=options)


driver.get("https://www.nseindia.com/")


sleep(randint(2, 8))

for element in range(1, 7):
    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable(
            (
                By.XPATH,
                f"/html/body/div[11]/div[1]/div[1]/div/div/section/div/div/div/nav/div/div/a[{element}]",
            )
        )
    ).click()
    for _ in range(50):
        driver.execute_script("window.scrollBy(0, 10);")
    for _ in range(50):
        driver.execute_script("window.scrollBy(0, -10);")

sleep(randint(2, 8))

WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.XPATH, f"/html/body/div[2]/div/div/div/ul/li[3]/a"))
).click()

sleep(randint(2, 8))

for _ in range(20):
    driver.execute_script("window.scrollBy(0, 20);")

for _ in range(20):
    driver.execute_script("window.scrollBy(0, -20);")


driver.find_element(
    By.XPATH, "/html/body/header/nav/div[1]/div[1]/div/div[1]/span/input"
).send_keys("Вот такой небольшой сценарий")

sleep(5)
