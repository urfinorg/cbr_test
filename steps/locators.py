from selenium.webdriver.common.by import By

class Locators(object):
    """A class for main page locators. All main page locators should come here"""
    
    GG_URL = "https://www.google.ru"
    GG_FIND_CBRF = "Центральный банк РФ"
    
    GG_INPUT = (By.NAME, 'q')
    GG_BUTTON =  (By.CSS_SELECTOR, "input[name='btnK']")
    GG_RESULTS = (By.XPATH, '//div[@class="r"]/a/h3')
    
    CBR_SITE_TITLE ="Центральный банк Российской Федерации"
    
    CBR_FORM_BODY = (By.ID, "MessageBody")
    CBR_SOME_TEXT = "случайный текст"
    
    CBR_WARNING_TEXT_ELEM = (By.CSS_SELECTOR, "#content>p")
    
    param_dict = {
        "CBR_RECIPIENT_LINK" : (By.LINK_TEXT, "Интернет-приемная"),
        "CBR_THANKS_LINK"    : (By.LINK_TEXT, "Написать благодарность"),
        
        "CBR_CHECKBOX"       : (By.CSS_SELECTOR, "#_agreementFlag"),
        "CBR_TOP_BUT"        : (By.CSS_SELECTOR, "span.burger"),
        
        "CBR_ABOUT_LINK"     : (By.LINK_TEXT, "О сайте"),
        "CBR_WARNING_LINK"   : (By.LINK_TEXT, "Предупреждение"),
        "CBR_CH_LANG_LINK"   : (By.LINK_TEXT, "EN"),       
    }
       

class SearchResultsPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    pass