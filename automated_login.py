from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

# TODO: Enter driver location
driver = webdriver.chrome.webdriver.WebDriver('. . .')

# TODO: Enter url
driver.get('. . .')
driver.find_element_by_id("cookieChoiceDismiss").click()
driver.find_element_by_link_text('Login').click()

login = driver.find_element_by_class_name('textfield')
# TODO: Enter login as string
login.send_keys(". . . ")
login.send_keys(Keys.ENTER)

password_key_1 = driver.find_element_by_xpath('//*[@id="mainForm"]/div[1]/div[1]/label').text
password_key_2 = driver.find_element_by_xpath('//*[@id="mainForm"]/div[1]/div[2]/label').text
password_key_3 = driver.find_element_by_xpath('//*[@id="mainForm"]/div[1]/div[3]/label').text

pin_key_1 = driver.find_element_by_xpath('//*[@id="mainForm"]/div[2]/div[1]/label').text
pin_key_2 = driver.find_element_by_xpath('//*[@id="mainForm"]/div[2]/div[2]/label').text
pin_key_3 = driver.find_element_by_xpath('//*[@id="mainForm"]/div[2]/div[3]/label').text

# TODO: Enter a password and pin as arrays
password_array = [. . .]
pin_array = [. . .]


def password_digit(password_key):

    password_number = []
    for word in password_key.split():
        if word.isdigit() == True:
            password_number.append(word)
            password_index = ''.join(password_number)
            for i in range(int(password_index) + 1):
                if password_index == str(i):
                    return password_array[i-1]


pw_1 = driver.find_element_by_id("inpPassword1")
pw_1.send_keys(password_digit(password_key_1))

pw_2 = driver.find_element_by_id("inpPassword2")
pw_2.send_keys(password_digit(password_key_2))

pw_3 = driver.find_element_by_id("inpPassword3")
pw_3.send_keys(password_digit(password_key_3))


def pin_digit(pin_key):

    pin_number = []
    for word in pin_key.split():
        if word.isdigit() == True:
            pin_number.append(word)
            pin_index = ''.join(pin_number)
            for i in range(int(pin_index) + 1):
                if pin_index == str(i):
                    return pin_array[i-1]


pin_1 = driver.find_element_by_id("inpPIN1")
pin_1.send_keys(pin_digit(pin_key_1))

pin_2 = driver.find_element_by_id("inpPIN2")
pin_2.send_keys(pin_digit(pin_key_2))

pin_3 = driver.find_element_by_id("inpPIN3")
pin_3.send_keys(pin_digit(pin_key_3))

#driver.find_element_by_id('bAction').click()