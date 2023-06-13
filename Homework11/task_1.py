# Перейти на https://sbis.ru/
# Перейти в раздел "Контакты"
# Найти баннер Тензор, кликнуть по нему
# Перейти на https://tensor.ru/
# Проверить, что есть блок новости "Сила в людях"
# Перейдите в этом блоке в "Подробнее" и убедитесь, что открывается https://tensor.ru/about
# Для сдачи задания пришлите код и запись с экрана прохождения теста


from selenium import webdriver
from time import sleep

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

sbis_site = 'https://sbis.ru/'

try:
    print(f'Перешли на сайт {sbis_site}')
    driver.get(sbis_site)
    assert driver.current_url == sbis_site, 'Неверно открыт сайт'
    sleep(2)

    print('Нашли и кликнули на ссылку "Контакты"')
    cont_btn = driver.find_element(By.CSS_SELECTOR, '.sbisru-Header__menu-item [href="/contacts"]')
    assert cont_btn.is_displayed(), 'Элемент не отображается'
    cont_btn.click()
    sleep(2)

    print('Нашли баннер "Тензор"')
    banner = driver.find_element(By.CSS_SELECTOR, '[src="/resources/NewDesign/pages/Contacts/images/logo.svg?x_module=23.3206-53"]')
    assert banner.is_displayed(), 'Баннер отсутствует'
    sleep(2)

    print('Кликнули по баннеру')
    banner.click()
    original_window = driver.current_window_handle
    for window_handle in driver.window_handles:
        if window_handle != original_window:
            driver.switch_to.window(window_handle)
            break

    print('Ссылка текущей вкладки tensor.ru')
    assert driver.current_url == 'https://tensor.ru/', 'Не перешли на сайт Тензор'
    sleep(2)

    print('Нашли блок новости "Сила в людях"')
    text_news = "Сила в людях"
    news = driver.find_element(By.XPATH, '//*[@id="container"]/div[1]/div/div[5]/div/div/div[1]')
    assert news.is_displayed()
    sleep(2)

    print('Закрытие информационной панели')
    info = driver.find_element(By.CSS_SELECTOR, '[class="tensor_ru-CookieAgreement__close icon-Close ws-flex-shrink-0 ws-flexbox ws-align-items-center"]')
    info.click()
    sleep(2)

    print('Ссылка О людях')
    link = driver.find_element(By.CSS_SELECTOR, '.tensor_ru-Index__card-text [href="/about"]')
    action = ActionChains(driver)
    action.move_to_element(link)
    action.perform()
    sleep(2)
    link.click()
    assert driver.current_url == 'https://tensor.ru/about', 'Не перешли на сайт Тензор, о людях'

    sleep(2)
    print('ОК')
finally:
    driver.quit()
