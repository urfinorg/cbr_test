
Feature: Checking goole.ru and cbr.ru

Scenario: Сheck some Scenario for CBR

    #1.Зашли на сайт google.ru
    Given open google
    
    #2.Проверили, что появилось поле “поиск”
    Then element INPUT exist
    
    #3. Ввели в поле поиск значение Центральный банк РФ
    Then enter text CBRF
  
    #4.Нажали на кнопку поиск в google
    Then push button find
    
    #5.Нашли ссылку “cbr.ru”
    Then select link cbr
    
    #6.Нажали на ссылку cbr.ru
    Then click link cbr 
    
    #7.Проверили, что открыт нужный сайт
    Then is cbr site
    
    #8.Нажали на ссылку Интернет-приемная
    Then click link by "CBR_RECIPIENT_LINK"
    
    #9.Открыли раздел Написать благодарность
    Then click link by "CBR_THANKS_LINK" 
    
    #10.В поле Ваша благодарность ввели значение “случайный текст”
    Then input some text
    
    #11.Поставили галочку “Я согласен”
    Then click link by "CBR_CHECKBOX"
    
    #12.Сделали скриншот
    Then make screenshot "screen_1.png"
    
    #13.Нажали на кнопку “Три полоски” #(Сверху слева, открывающая меню)
    Then click link by "CBR_TOP_BUT"
    
    #14.Нажали на раздел О сайте
    Then click link by "CBR_ABOUT_LINK"
    
    #15.Нажали на ссылку предупреждение
    Then click link by "CBR_WARNING_LINK"
    
    #16.Запомнили текст предупреждения
    Then get warning text
    
    #17.Сменили язык страницы на en (сверху выбор есть)
    Then click link by "CBR_CH_LANG_LINK"
    
    #18.Проверили, что текст отличается от запомненного текста ранее
    Then get NEW warning text
    
    #19.Сделали скриншот
    Then make screenshot "screen_2.png"  
  
    Then close browser and SEND_MAIL and DELETE_FILES
  
  
  
  
  
