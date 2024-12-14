from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


driver = webdriver.Firefox()

driver.get("https://kinopoisk.ru/")

title = driver.title
sleep(60)  # Это время на решение капчи.

driver.find_element(By.CSS_SELECTOR, ".styles_loginButton__LWZQp").click()
sleep(5)

driver.find_element(By.XPATH, '//*[@id="passp-field-login"]').send_keys("example@yandex.ru")
sleep(5)

driver.find_element(By.XPATH, '//*[@id="passp:sign-in"]').click()
sleep(5)

driver.find_element(By.XPATH, '//*[@id="passp-field-passwd"]').send_keys("P@ssw0rd")
sleep(5)

driver.find_element(By.XPATH, '//*[@id="passp:sign-in"]').click()
sleep(5)

driver.quit()
