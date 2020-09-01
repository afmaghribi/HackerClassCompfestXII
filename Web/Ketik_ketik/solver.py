from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep

browser = webdriver.Firefox()
browser.set_window_size(900,900)
browser.get('http://128.199.104.41:25894/')
while(1):
	browser.find_element_by_xpath('//input[1]').send_keys('aku ingin menjadi hacker handal aku harus terus berlatih pantang menyerah dapatkan flagnya aku ingin menjadi legenda aku ingin bisa ngehack ig aku akan menggunakan keahlianku untuk kebaikan ')
	sleep(4)
	ada = browser.find_element_by_tag_name('body').text
	if "No flag for you!" in ada:
		browser.find_element_by_tag_name('button').send_keys(Keys.RETURN)
	else:
		break

