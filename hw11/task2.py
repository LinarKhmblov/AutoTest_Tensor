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
    driver.maximize_window()
    driver.get(sbis_site)
    sleep(1)
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys('скрипач', Keys.ENTER)
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys('скрипка11', Keys.ENTER)
    sleep(1)
    driver.get('https://fix-online.sbis.ru/page/contacts/')
    sleep(1)
    find_user = driver.find_element(By.CSS_SELECTOR, '[data-qa="tile-container"] [item-key="07131b5d-9a5a-4075-8c33-8f7055844bfe"]')
    action_chains = ActionChains(driver)
    action_chains.move_to_element(find_user)
    action_chains.context_click(find_user)
    action_chains.perform()
    sleep(1)
    add_new_message = driver.find_element(By.CSS_SELECTOR, '[data-qa="item"] [title="Отправить сообщение"] [class="ws-ellipsis controls-Menu__content-wrapper_width"]')
    add_new_message.click()
    sleep(1)
    text_input = driver.find_element(By.CSS_SELECTOR, '[class="textEditor_Viewer__Paragraph"]')
    text_input.send_keys('test')
    sleep(1)
    send_btn = driver.find_element(By.CSS_SELECTOR, '.msg-send-editor-send')
    send_btn.click()
    sleep(1)
    dialogs = driver.find_element(By.CSS_SELECTOR, '[name="tabdialogs"]')
    dialogs.click()
    sleep(1)
    new_message = driver.find_element(By.CSS_SELECTOR, '[data-qa="item"] .controls-ListView__itemContent .msg-entity-text')
    assert new_message.is_displayed()
    action_chains.move_to_element(new_message).perform()
    action_chains.context_click(new_message).perform()
    sleep(1)
    delete_btn = driver.find_element(By.CSS_SELECTOR, '[data-target="menu_item_deleteToArchive"]')
    delete_btn.click()
    sleep(1)
    empty_folder_title = driver.find_element(By.CSS_SELECTOR, '.hint-Template__text_message')
    assert empty_folder_title.is_displayed()
finally:
    driver.quit()
