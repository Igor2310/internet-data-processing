from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


s = Service('./chromedriver')
driver = webdriver.Chrome(service=s)
driver.implicitly_wait(8)

driver.get('https://e.mail.ru/login')

driver.get(driver.find_element(By.TAG_NAME, 'iframe').get_attribute('src'))
if driver.find_element(By.XPATH, "//div[@class='save-auth-field-wrap']").get_attribute('data-checked'):
    driver.find_element(By.XPATH, "//div[@class='save-auth-field-wrap']").click()

elem = driver.find_element(By.XPATH, "//input[@name='username']")
elem.send_keys("study.ai_172@mail.ru")
driver.find_element(By.XPATH, "//button[@data-test-id='next-button']").click()

elem = driver.find_element(By.XPATH, "//input[@name='password']")
elem.send_keys("Ferrum123!")
driver.find_element(By.XPATH, "//button[@data-test-id='submit-button']").click()

driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")

print(len(driver.find_elements(By.XPATH, "//div[@class='llc__background']")))
