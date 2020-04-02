from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
import requests
from bs4 import BeautifulSoup
import time
import xlsxwriter
from autogui import booya


print('\n')
print('\n')

# get data
owner_first_name = input("Business Owner First Name: ")
owner_last_name = input("Business Owner Last Name: ")
ssn1, ssn2, ssn3 = input("Social Security #: ").replace('-', ' ').split()
print('Business Address')
business_street = input("Street: ").title()
business_city = input("City: ").title()
business_zip_code = input("Zip: ")
business_state = input('State: ').capitalize()
phone_number = input('Phone Number: ')


print('\n')
print('\n')


# initiate driver
driver = webdriver.Chrome('/Users/anthonymota/Downloads/chromedriver')


# get website
driver.get('https://sa.www4.irs.gov/modiein/individual/index.jsp')
driver.switch_to.alert.accept()
driver.find_element_by_xpath('//*[@id="topcontent"]/form/div[5]/input').click()
driver.find_element_by_xpath('//*[@id="sole"]').click()
driver.find_element_by_xpath(
    '//*[@id="individual-leftcontent"]/form/div[16]/input').click()
driver.find_element_by_xpath('//*[@id="sole"]').click()
driver.find_element_by_xpath(
    '//*[@id="individual-leftcontent"]/form/div[6]/input').click()
driver.find_element_by_xpath(
    '//*[@id="individual-leftcontent"]/form/div[2]/input').click()
driver.find_element_by_xpath('//*[@id="newbiz"]').click()
driver.find_element_by_xpath(
    '//*[@id="individual-leftcontent"]/form/div[11]/input').click()
driver.find_element_by_xpath(
    '//*[@id="applicantFirstName"]').send_keys(owner_first_name)
driver.find_element_by_xpath(
    '//*[@id="applicantLastName"]').send_keys(owner_last_name)
driver.find_element_by_xpath('//*[@id="applicantSSN3"]').send_keys(ssn1)
driver.find_element_by_xpath('//*[@id="applicantSSN2"]').send_keys(ssn2)
driver.find_element_by_xpath('//*[@id="applicantSSN4"]').send_keys(ssn3)
driver.find_element_by_xpath('//*[@id="iamthird"]').click()
driver.find_element_by_xpath(
    '//*[@id="individual-leftcontent"]/form/div[5]/input').click()
booya()
driver.find_element_by_xpath('//*[@id="rightcontent"]/input').click()
driver.find_element_by_xpath('//*[@id="yes"]').click()
driver.find_element_by_xpath('//*[@id="rightcontent"]/input')
driver.find_element_by_xpath(
    '//*[@id="thirdPartyFirstName"]').send_keys(owner_first_name)
driver.find_element_by_xpath(
    '//*[@id="thirdPartyLastName"]').send_keys(owner_last_name)
driver.find_element_by_xpath(
    '//*[@id="thirdPartyStreet"]').send_keys("8072 Archibald Ave")
driver.find_element_by_xpath('Alta Loma')
Select(driver.find_element_by_xpath(
    '//*[@id="thirdPartyState"]')).select_by_index(5)
driver.find_element_by_xpath('//*[@id="thirdPartyZipCode"]').send_keys('91730')
driver.find_element_by_xpath('//*[@id="thirdPartyFirst3"]').send_keys('909')
driver.find_element_by_xpath('//*[@id="thirdPartyMiddle3"]').send_keys('204')
driver.find_element_by_xpath('//*[@id="thirdPartyLast4"]').send_keys('1057')
driver.find_element_by_xpath(
    '//*[@id="individual-leftcontent"]/form/div[3]/input').click()
driver.find_element_by_xpath(
    '//*[@id="verify-rightcontent"]/table/tbody/tr/td/input').click()
driver.find_element_by_xpath(
    '//*[@id="physicalAddressStreet"]').send_keys(business_street)
driver.find_element_by_xpath(
    '//*[@id="physicalAddressCity"]').send_keys(business_city)
Select(driver.find_element_by_xpath(
    '//*[@id="physicalAddressState"]')).select_by_index(5)
driver.find_element_by_xpath(
    '//*[@id="physicalAddressZipCode"]').send_keys(business_zip_code)
