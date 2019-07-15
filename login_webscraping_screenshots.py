from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests

# paths
CHROME_PATH = ''
CHROMEDRIVER_PATH = ''

# Window size
WINDOW_SIZE = "1200,1200"

# Chrome Options
chrome_options = Options()
chrome_options.add_argument("--headless")
chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
chrome_options.binary_location = CHROME_PATH

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                          options=chrome_options)

start_page = ''

driver.get(start_page)

driver.find_element_by_id("cookieChoiceDismiss").click()
driver.find_element_by_link_text('Login').click()

login = driver.find_element_by_class_name('textfield')

# TODO: Enter login as string
login.send_keys('')
login.send_keys(Keys.ENTER)

password_key_1 = driver.find_element_by_xpath('//*[@id="mainForm"]/div[1]/div[1]/label').text
password_key_2 = driver.find_element_by_xpath('//*[@id="mainForm"]/div[1]/div[2]/label').text
password_key_3 = driver.find_element_by_xpath('//*[@id="mainForm"]/div[1]/div[3]/label').text

pin_key_1 = driver.find_element_by_xpath('//*[@id="mainForm"]/div[2]/div[1]/label').text
pin_key_2 = driver.find_element_by_xpath('//*[@id="mainForm"]/div[2]/div[2]/label').text
pin_key_3 = driver.find_element_by_xpath('//*[@id="mainForm"]/div[2]/div[3]/label').text

# TODO: Enter a password and pin
password_array = list('')
pin_array = list('')


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

driver.find_element_by_xpath('//*[@id="bAction"]').click()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="btnProceed"]').click()

time.sleep(2)

# logged in
# Getting list of links from all divs

home_page = driver.current_url

print(home_page)

source = requests.get(home_page).text
soup = BeautifulSoup(source, 'html.parser')

links_list = []
titles_list = []
data = soup.find('div', class_='half-width')
print(data)

for div in data:
    links = div.find_all('a')
    titles = div.find_all('title')
    for a in links:
        # print(a['href'])
        links_list.append('' + a['href'])
        titles_list.append(a['title'])

for i in range(len(titles_list)):
    print(titles_list[i] + ' --> ' + links_list[i])

# Taking screenshot of each page

for link in links_list:

    driver.get(link)
    time.sleep(2)

    link_string = link.split('://')[1]
    filename = link_string.replace('/', '_')
    image = filename.replace('.', '_') + ".png"

    driver.save_screenshot(image)

driver.close()