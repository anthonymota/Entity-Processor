from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from data import *

# initiate driver
driver = webdriver.Chrome('/Users/anthonymota/Downloads/chromedriver')
driver.get('https://llcbizfile.sos.ca.gov/SI')


#begin
driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div[1]/fieldset/div/span[2]/input').click()
driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[3]/div[1]/div/div/input').send_keys(entity_number)
driver.find_element_by_xpath('//*[@id="Button_Search"]').click()
driver.find_element_by_xpath('//*[@id="enitityTable"]/tbody/tr/td[4]/a').click()
driver.find_element_by_xpath('//*[@id="btnContinueFiling"]').click()
driver.find_element_by_xpath('//*[@id="btnIAccept"]').click()
driver.find_element_by_xpath('//*[@id="AddressLine1"]').send_keys(business_street)
driver.find_element_by_xpath('//*[@id="City"]').send_keys(business_city)
state=Select(driver.find_element_by_xpath('//*[@id="State"]'))
state.select_by_value('CA')
driver.find_element_by_xpath('//*[@id="ZipCode"]').send_keys(business_zip_code)
country=Select(driver.find_element_by_xpath('//*[@id="Country"]'))
country.select_by_value('US')
driver.find_element_by_xpath('//*[@id="btnContinue"]').click()
driver.find_element_by_xpath('//*[@id="IsAddressSameAsPrincipalAddress"]').click()
driver.find_element_by_xpath('//*[@id="btnContinue"]').click()
driver.find_element_by_xpath('//*[@id="IsAddressSameAsPrincipalAddress"]').click()
driver.find_element_by_xpath('//*[@id="btnContinue"]').click()

#manager
driver.find_element_by_xpath('//*[@id="FirstName"]').send_keys(owner_first_name)
driver.find_element_by_xpath('//*[@id="LastName"]').send_keys(owner_last_name)
driver.find_element_by_xpath('//*[@id="AddressLine1"]').send_keys(business_street)
driver.find_element_by_xpath('//*[@id="City"]').send_keys(business_city)
state2=Select(driver.find_element_by_xpath('//*[@id="State"]'))
state2.select_by_value('CA')
driver.find_element_by_xpath('//*[@id="ZipCode"]').send_keys(business_zip_code)
country2=Select(driver.find_element_by_xpath('//*[@id="Country"]'))
country2.select_by_value('US')
driver.find_element_by_xpath('//*[@id="btnContinue"]').click()
driver.find_element_by_xpath('//*[@id="btnContinue"]').click()

#agent
driver.find_element_by_xpath('//*[@id="FirstName"]').send_keys(owner_first_name)
driver.find_element_by_xpath('//*[@id="LastName"]').send_keys(owner_last_name)
driver.find_element_by_xpath('//*[@id="AddressLine1"]').send_keys(business_street)
driver.find_element_by_xpath('//*[@id="City"]').send_keys(business_city)
driver.find_element_by_xpath('//*[@id="ZipCode"]').send_keys(business_zip_code)
driver.find_element_by_xpath('//*[@id="btnContinue"]').click()

#business
driver.find_element_by_xpath('//*[@id="BusinessDescription"]').send_keys(type_of_business)
driver.find_element_by_xpath('//*[@id="btnContinue"]').click()

#ceo
#ask mom if necessary
driver.find_element_by_xpath('//*[@id="btnContinue"]').click()

#review
driver.find_element_by_xpath('//*[@id="EmailAddress"]').send_keys(organizer_email)
driver.find_element_by_xpath('//*[@id="ConfirmEmailAddress"]').send_keys(organizer_email)
driver.find_element_by_xpath('//*[@id="btnContinue"]').click()
