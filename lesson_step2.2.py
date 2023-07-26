import time #модуль для работы со временем в Python.
from selenium import webdriver #импортировать пакет Selenium WebDriver.
from selenium.webdriver.common.by import By #импортируем метод для поиска элементов
import math

try:
    link = "http://suninjuly.github.io/get_attribute.html"
    browser = webdriver.Chrome()
    browser.get(link)


    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))


    x_element = browser.find_element(By.XPATH, "//div//img[@id='treasure']")
    x = x_element.get_attribute("valuex") #Найдём атрибут "valuex" с помощью встроенного метода get_attribute
    y = calc(x)# найти элемент и взять значение текст находящийся в этом поле и посчитать функцию калькулятор с нашим найденным значением из текста

    input1 = browser.find_element(By.XPATH, "//input[@id='answer']")
    input1.send_keys(y)  # найти поле и вставить в него значение у

    option1 = browser.find_element(By.XPATH, "//input[@type='checkbox']")
    option1.click()  # найти чекбокс и нажать на него

    option1 = browser.find_element(By.XPATH, "//input[@type='radio' and @value='robots']")
    option1.click()  # найти радиобаттон и переключить его

    button = browser.find_element(By.XPATH, "//button[@type='submit']")
    button.click()# найти кнопку и нажать на нее

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

# не забываем оставить пустую строку в конце файла
# не забываем оставить пустую строку в конце файла