from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


def find_goods(my_driver):

    element = WebDriverWait(my_driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'Полотно для заваривания чая'))
    )
    element.click()

    buy = my_driver.find_element_by_id("skuadd")
    buy.click()

    basket = WebDriverWait(my_driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, "Перейти в корзину"))
    )
    basket.click()

    menu = my_driver.find_element_by_class_name('md-menu__hamburger')
    menu.click()

    ceremony = WebDriverWait(my_driver, 10).until(
        EC.presence_of_element_located((By.PARTIAL_LINK_TEXT, 'ЧАЙНЫЕ ЦЕРЕМОНИИ'))
    )
    ceremony.click()

    my_driver.execute_script("window.scrollTo(0, 2800)")

    time.sleep(5)

    my_driver.switch_to.frame(my_driver.find_element_by_class_name("uCalc-frame_132406"))

    cancel_ceremony = my_driver.find_element_by_xpath("//div[@data-checkbox='0']")
    cancel_ceremony.click()

    choose_ceremony = my_driver.find_element_by_xpath("//div[@data-checkbox='2']")
    choose_ceremony.click()

    change = my_driver.find_element_by_xpath("//div[@data-radio='1']")
    change.click()

    my_driver.switch_to.default_content()



PATH = "/home/tais/chromedriver"
driver = webdriver.Chrome(PATH)

driver.get('https://process-tea.ru/')
link = driver.find_element_by_link_text('Купить чай, подарки. посуду, утварь')
link.click()

try:
    find_goods(driver)
except Exception as e:
    print(e)
finally:
    time.sleep(15)
    driver.close()
