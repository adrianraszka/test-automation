# from selenium import webdriver
# import time
# from selenium.webdriver.common.keys import Keys
# # TODO: enter an url
# driver = webdriver.chrome.webdriver.WebDriver('C:\\Users\\P10481111\\Desktop\\untitled1\\chromedriver')
#
# driver.get('https://qa.hartlinkonline.co.uk/unilever/hofq.chi/wui/tilepgui.html')
# driver.find_element_by_id("cookieChoiceDismiss").click()
# driver.find_element_by_link_text('Login').click()
#
# login = driver.find_element_by_class_name('textfield')
# login.send_keys("Pensioner8Unilever")
# login.send_keys(Keys.ENTER)
#
# password_key_1 = driver.find_element_by_xpath('//*[@id="mainForm"]/div[1]/div[1]/label').text
# password_key_2 = driver.find_element_by_xpath('//*[@id="mainForm"]/div[1]/div[2]/label').text
# password_key_3 = driver.find_element_by_xpath('//*[@id="mainForm"]/div[1]/div[3]/label').text
#
# # TODO: enter a password as array
password_array = ['S', 'h', 'e', 'f', 'f', 'i', 'e', 'l', 'd', '1']

password_key_1 = ("Enter character 3 from your Password:")
password_key_2 = ("Enter character 5 from your Password:")
password_key_3 = ("Enter character 8 from your Password:")

def password_digit(password_key):

    password_number = []
    for word in password_key.split():
        if word.isdigit() == True:
            password_number.append(word)
            password_index = ''.join(password_number)
            for i in range(int(password_index) + 1):
                if password_index == str(i):
                    return password_array[i-1]



password_digit(password_key_1)
password_digit(password_key_2)
password_digit(password_key_3)

