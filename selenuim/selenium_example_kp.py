"""
    Тест поиска.
"""
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Firefox()

driver.get("https://kinopoisk.ru/")

title = driver.title
timeout = 60  # Это время на решение капчи.

try:  # Поставить галку "Я не робот".
    driver.find_element(By.CSS_SELECTOR, ".CheckboxCaptcha-Button").click()
except NoSuchElementException:
    pass

try:  # Закрыть коммуникацию.
    WebDriverWait(driver, timeout).until(
        EC.presence_of_element_located((By.CSS_SELECTOR,
                                        ".styles_root__EjoL7"))
    )
    driver.find_element(By.CSS_SELECTOR, ".styles_root__EjoL7").click()
except TimeoutException:
    pass
except NoSuchElementException:
    pass

driver.find_element(By.TAG_NAME, "input").send_keys("Bad Sisters")
sleep(5)

driver.find_element(By.CSS_SELECTOR, ".search-form-submit-button__icon").\
                    click()
sleep(5)

result_text = driver.find_element(By.CSS_SELECTOR, ".search_results_topText").\
                                  text
result_list = result_text.split(": ")

driver.quit()

print(f"Количество результатов по запросу {int(result_list[2])}")
