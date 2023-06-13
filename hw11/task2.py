# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains



sbis_site = 'https://fix-online.sbis.ru/'
driver = webdriver.Chrome()
try:
    driver.get(sbis_site)
    sleep(2)
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys('скрипач', Keys.ENTER)
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys('скрипка11', Keys.ENTER)
    sleep(5)
    # contacts_btn = driver.find_element(By.CSS_SELECTOR, '[data-name="contacts"]')
    # contacts_btn.click()
    new_contact_btn = driver.find_element(By.CSS_SELECTOR, '[data-name="contacts"] .NavigationPanels-Counter__arrow_icon')
    new_contact_btn.click()
    new_message_btn = driver.find_element(By.CSS_SELECTOR, '.msg-informer-contacts__toolbar-button-message')
    assert new_message_btn.is_displayed()
    # new_message_btn.click()
    # sleep(5)
finally:
    driver.quit()



 # action_chains = ActionChains(driver)
    # action_chains.double_click(contacts_btn).perform()