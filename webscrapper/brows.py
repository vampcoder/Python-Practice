from selenium import webdriver
import time

browser = webdriver.Firefox()
browser.get('https://gmail.com')
email = browser.find_element_by_id('Email')
email.send_keys('IRM2013010@iiita.ac.in')
email.submit()
time.sleep(1)
passwd = browser.find_element_by_id('Passwd')
passwd.send_keys('9044172433')
passwd.submit()