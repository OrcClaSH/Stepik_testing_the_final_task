# Добавил импорт для аргумента браузера
from selenium.webdriver import Remote as RemoteWebDriver


class BasePage():
    # Проставил класс для агрумента браузера, в IDE 
    # будут всплывать подсказки методов
    def __init__(self, browser: RemoteWebDriver, url):
        self.browser = browser
        self.url = url
    
    def open(self):
        self.browser.get(self.url)
