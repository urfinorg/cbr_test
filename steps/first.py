from behave import *

from selenium import webdriver
from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options

from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

import time
import os

from send_mail import send_mail_by_yandex

from locators import Locators

options = Options()
options.headless = True

l_loc = Locators()

#1.Зашли на сайт google.ru
@given('open google')
def step(context):
    context.browser = webdriver.Firefox(options=options)
    context.browser.maximize_window()
    context.browser.get(l_loc.GG_URL)
    
    context.screen_files_list = []

#2.Проверили, что появилось поле “поиск”,
@then('element INPUT exist')
def step(context):
    exist = True
    try:
        context.s_elem = context.browser.find_element(*l_loc.GG_INPUT)
    except NoSuchElementException:
        exist = False
    assert exist, 'Element "q" not exist'
    print('OK, element "q" existed')
    
#3. Ввели в поле поиск значение Центральный банк РФ
@then('enter text CBRF')
def step(context):
    context.s_elem.send_keys(l_loc.GG_FIND_CBRF)

    
#4.Нажали на кнопку поиск в google
@then('push button find')
def step(context):    
    WebDriverWait(context.browser, 6).until(
        EC.element_to_be_clickable(l_loc.GG_BUTTON)
    )
    context.browser.find_element(*l_loc.GG_BUTTON).click()
    
#5.Нашли ссылку “cbr.ru”
@then('select link cbr')
def step(context):
    context.results = context.browser.find_elements(*l_loc.GG_RESULTS)


#6.Нажали на ссылку cbr.ru
@then('click link cbr')
def step(context):
    context.results[0].click()
    
    
#7.Проверили, что открыт нужный сайт
@then('is cbr site')
def step(context):
    
    new_browser_window = context.browser.window_handles[1]
    context.browser.switch_to.window(new_browser_window)
    
    WebDriverWait(context.browser, 12).until(
        EC.element_to_be_clickable((By.ID, 'footer'))
    )

    assert (context.browser.title == l_loc.CBR_SITE_TITLE), 'Not cbr site'

    
#8.Нажали на ссылку Интернет-приемная
@then('click link by "{str_param_dict}"')
def step(context, str_param_dict):
    #next_link = context.browser.find_element(*l_loc.CBR_RECIPIENT_LINK)
    next_link = context.browser.find_element(*l_loc.param_dict[str_param_dict])
    next_link.click()
    

#10.В поле Ваша благодарность ввели значение “случайный текст”
@then('input some text')
def step(context):
    
    #WebDriverWait(context.browser, 3).until(
    #    EC.element_to_be_clickable(l_loc.CBR_FORM_BODY)
    #)
    
    elem = context.browser.find_element(*l_loc.CBR_FORM_BODY)
    elem.clear()
    elem.send_keys(l_loc.CBR_SOME_TEXT)
    

#12.Сделали скриншот
@then('make screenshot "{file_name}"')
def step(context, file_name):
    context.browser.save_screenshot(file_name)
    context.screen_files_list.append(file_name)

#16.Запомнили текст предупреждения
@then('get warning text')
def step(context):
    elem = context.browser.find_element(*l_loc.CBR_WARNING_TEXT_ELEM)
    context.warning_text = elem.text     
    
    
#18.Проверили, что текст отличается от запомненного текста ранее
@then('get NEW warning text')
def step(context):
    elem = context.browser.find_element(*l_loc.CBR_WARNING_TEXT_ELEM)
    new_text = elem.text
    #Если текст НЕ изменился случится assert
    assert (context.warning_text != new_text), 'No change in text'  
    

@then("close browser and SEND_MAIL and DELETE_FILES")
def step(context):
    context.browser.quit()
     
    
    #send_mail_by_yandex(username="user@yandex.ru", password="pass_of_user", \
    #                toaddrs_list=["to_addres@first.ru"], \
    #                msg_text="Scenario screens", \
    #                fromaddr="user@yandex.ru", \
    #                subject="Checking goole.ru and cbr.ru", \
    #                attachment_path_list = context.screen_files_list )
    
    
    #Удаляем скриншеты
    #for file in context.screen_files_list:
    #    os.remove(file)
        
    
