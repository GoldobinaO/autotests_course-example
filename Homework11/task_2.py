# Авторизоваться на сайте https://fix-online.sbis.ru/
# Перейти в реестр Контакты
# Отправить сообщение самому себе
# Убедиться, что сообщение появилось в реестре
# Удалить это сообщение и убедиться, что удалили
# Для сдачи задания пришлите код и запись с экрана прохождения теста

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver import Keys, ActionChains

driver = webdriver.Chrome()
sbis_site = 'https://fix-online.sbis.ru/'

try:
    print(f'Перешли на сайт {sbis_site}')
    driver.get(sbis_site)
    sleep(3)

    print('Залогинились на сайт')
    user_login, user_password = 'СхемаСидоров', 'СхемаСидоров123'
    login = driver.find_element(By.CSS_SELECTOR, '[name="Login"]')
    login.send_keys(user_login, Keys.ENTER)
    assert login.get_attribute('value') == user_login
    sleep(1)
    password = driver.find_element(By.CSS_SELECTOR, '[name="Password"]')
    password.send_keys(user_password, Keys.ENTER)

    sleep(5)
    print('Перешли в реестр Контакты')
    contact = driver.find_element(By.CSS_SELECTOR, '[data-name="contacts"]')
    contact.click()
    sleep(1)
    contact_two = driver.find_element(By.CSS_SELECTOR, '[class="NavigationPanels-SubMenu__headTitle   NavigationPanels-SubMenu__title-with-separator NavigationPanels-Accordion__prevent-default"]')
    contact_two.click()
    sleep(5)

    print('Нашли и кликнули кнопку "+"')
    btn = driver.find_element(By.CSS_SELECTOR, '[class="controls-Button__icon controls-BaseButton__icon controls-icon_size-m controls-icon_style-default controls-icon icon-RoundPlus"]')
    btn.click()
    sleep(5)

    print('Вводим ФИ для поиска')
    user = 'Сидоров Максим'
    find = driver.find_element(By.CSS_SELECTOR, '.controls-Render__field .controls-Field')
    find.send_keys(user, Keys.ENTER)
    sleep(1)

    print('Выбираем пользователя')
    user_tile = driver.find_element(By.CSS_SELECTOR, '.msg-addressee-selector__addressee')
    user_tile.click()
    sleep(2)

    print('Ввод сообщения')
    text_to_send = 'Сообщение самому себе'
    text_editor = driver.find_element(By.CSS_SELECTOR, '.textEditor_slate_Field')
    text_editor.send_keys(text_to_send)
    sleep(1)

    print('Отправка сообщения')
    send_btn = driver.find_element(By.CSS_SELECTOR, '[data-qa="msg-send-editor__send-button"]')
    send_btn.click()
    sleep(5)

    print('Проверка наличия сообщения')
    find_msg = driver.find_element(By.CSS_SELECTOR, '.controls-Render__field .controls-Field')
    find_msg.send_keys(text_to_send, Keys.ENTER)
    sleep(3)
    eye = driver.find_element(By.CSS_SELECTOR, '[class="msg-entity-info__unread-icon icon-16 ws-flex-shrink-0 ws-flex-grow-0 ws-align-self-center icon-Show icon-hover"]')
    assert eye.is_displayed(), 'Сообщение не найдено'

    print('Удаление сообщения')
    action_chains = ActionChains(driver)
    action_chains.context_click(eye)
    action_chains.perform()
    sleep(3)

    del_btn = driver.find_element(By.XPATH, '//*[@id="popup"]/div[1]/div/div/div[1]/div/div/div/div/div/div[1]/div/div/div[6]')
    del_btn.click()
    sleep(3)

    print('Проверка, что сообщение удалено')
    boy = driver.find_element(By.CSS_SELECTOR, '[data-qa="hint-Template__imageWrapper"]')
    assert boy.is_displayed(), 'Сообщение не было удалено'

    sleep(5)
    print('ОК')
finally:
    driver.quit()

