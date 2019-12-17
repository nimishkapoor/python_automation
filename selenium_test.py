from selenium import webdriver
from selenium.webdriver.common.keys import Keys
browser=webdriver.Firefox()
browser.get('http://www.seleniumhq.org')
elem=browser.find_element_by_link_text('Downloads')
print(elem.text)
print(elem.get_attribute('href'))
elem.click()
elem=browser.find_element_by_link_text('Projects')
elem.click()
searchbar=browser.find_element_by_id('gsc-i-id1')
searchbar.send_keys('download')
searchbar.send_keys(Keys.ENTER)