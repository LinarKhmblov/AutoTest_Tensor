# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


sbis_site = 'https://sbis.ru/'
driver = webdriver.Chrome()

try:
    driver.get(sbis_site)
    sleep(2)
    contact_btn = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item-1')
    contact_btn.click()
    sleep(2)
    tensor_logo_btn = driver.find_element(By.CSS_SELECTOR, '.sbisru-Contacts__logo-tensor')
    tensor_logo_btn.click()
    driver.switch_to.window(driver.window_handles[1])
    sleep(2)
    block_title = "Сила в людях"
    blocks = driver.find_elements(By.CSS_SELECTOR, '.s-Grid-col--sm12')
    news_block = blocks[2]
    assert block_title in news_block.text, 'Нет такого заголовка'
    close_banner = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-CookieAgreement__close')
    close_banner.click()
    about_btn = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__card-text [href="/about"]')
    about_btn.click()
    driver.switch_to.window(driver.window_handles[1])
    sleep(2)
    assert driver.current_url == 'https://tensor.ru/about'
finally:
    driver.quit()