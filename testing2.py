from selenium import webdriver

browser = webdriver.Chrome('C:\\Users\\007\\Desktop\\testingA\\files\\webdriver')

browser.get('http://www.seleniumhq.org/')
browser.find_element_by_link_text('Download')
elem = browser.find_element_by_link_text('Download')
elem.get_attribute('href')
elem.click()

elem = browser.find_element_by_link_text('Projects')
elem.click()

searchBar = browser.find_element_by_id('q')
elem = browser.find_element_by_link_text('Projects')
elem.click()
searchBar = browser.find_element_by_id('q')
searchBar.send_keys('download')

from selenium.webdriver.common.keys import Keys

searchBar.send_keys('Keys.Enter')