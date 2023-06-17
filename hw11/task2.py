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
    find_user = driver.find_element(By.CSS_SELECTOR, '[data-qa="item"] [title="if working_hours > 8: print"]')
    action_chains = ActionChains(driver)
    action_chains.move_to_element(find_user)
    action_chains.context_click(find_user)
    action_chains.perform()
    sleep(1)
    add_new_message = driver.find_element(By.CSS_SELECTOR, '[data-qa="item"] [title="Отправить сообщение"] [class="ws-ellipsis controls-Menu__content-wrapper_width"]')
    add_new_message.click()
    sleep(2)
    text_input = driver.find_element(By.CSS_SELECTOR, '[data-qa="textEditor_slate_Field"]')
    text_input.send_keys('test')
    sleep(2)
    send_btn = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')
    send_btn.click()
    sleep(2)
    dialogs = driver.find_element(By.CSS_SELECTOR, '[name="tabdialogs"]')
    dialogs.click()
    sleep(3)
    message_to_find = 'test'
    messages = driver.find_elements(By.CSS_SELECTOR, '.Hint-ListWrapper .controls-BaseControl .controls-ListViewV')
    new_message = messages[0]
    assert message_to_find in new_message.text, 'Нет такого сообщения'
    action_chains.move_to_element(messages[0]).perform()
    action_chains.context_click(messages[0]).perform()
    sleep(1)
    delete_btn = driver.find_element(By.CSS_SELECTOR, '[data-target="menu_item_deleteToArchive"]')
    delete_btn.click()
    sleep(1)
    assert messages[0].is_displayed(), 'Сообщение удалено'
finally:
    driver.quit()
