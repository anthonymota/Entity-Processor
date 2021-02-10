from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options

def run(entity_number,business_street,business_city,business_zip_code,owner_first_name,owner_last_name,type_of_business,organizer_email):
    # initiate driver
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(chrome_options=chrome_options)
    driver.get('https://llcbizfile.sos.ca.gov/SI')


    #begin
    driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[2]/div/div[1]/fieldset/div/span[2]/input').click()
    driver.find_element_by_xpath('/html/body/div[1]/div/div/form/div[3]/div[1]/div/div/input').send_keys(entity_number)
    driver.find_element_by_xpath('//*[@id="Button_Search"]').click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="enitityTable"]/tbody/tr/td[4]/a'))).click()
    driver.find_element_by_xpath('//*[@id="btnContinueFiling"]').click()
    driver.find_element_by_xpath('//*[@id="btnIAccept"]').click()
    driver.find_element_by_xpath('//*[@id="CompleteFilingOpt"]').click()
    driver.find_element_by_xpath('//*[@id="btnContinue"]').click()
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
    time.sleep(120)