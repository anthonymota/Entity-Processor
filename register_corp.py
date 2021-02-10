from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time
import xlsxwriter

def run(legal_company_name,business_street,business_city,business_zip_code):
    mailing_address='yes'
    print('\n')
    print('\n')

    #initiate driver
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
   # driver = webdriver.Chrome()
    driver.get('https://corpbizfile.sos.ca.gov/Registration')
    driver.switch_to.frame(0)

    #begin form
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='element192__Option_1']").click()
    driver.find_element_by_xpath('//*[@id="form-section-0"]/div[5]/input[1]').click()
    #form2
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="element1"]').send_keys(legal_company_name)
    driver.find_element_by_xpath('//*[@id="form-section-1"]/div[9]/input[2]').click()
    #form3
    time.sleep(2)
    country=Select(driver.find_element_by_xpath('//*[@id="element80"]'))
    country.select_by_visible_text('United States of America')
    driver.find_element_by_xpath('//*[@id="element10"]').send_keys(business_street)
    driver.find_element_by_xpath('//*[@id="element11"]').send_keys(business_city)
    state=Select(driver.find_element_by_xpath('//*[@id="element81"]'))
    state.select_by_visible_text('California')
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="element13"]').send_keys(business_zip_code)
    if mailing_address=='yes':
        driver.find_element_by_xpath('//*[@id="element15_Option_1"]').click()
    driver.find_element_by_xpath('//*[@id="form-section-2"]/div[18]/input[2]').click()
    #form4
    time.sleep(2)
    driver.find_element_by_xpath('//*[@id="element16_Option_2"]').click()
    driver.find_element_by_xpath('//*[@id="form-section-3"]/div[17]/input[2]').click()
    #form5
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//*[@id="element31"]'))).send_keys('2')
    driver.find_element_by_xpath('//*[@id="element199_Option_1"]').click()
    driver.find_element_by_xpath('//*[@id="form-section-4"]/div[12]/input[2]').click()
    #form6
    driver.find_element_by_xpath('//*[@id="element70"]').click()
    driver.find_element_by_xpath('//*[@id="element380"]').send_keys('example')
    driver.find_element_by_xpath('//*[@id="element382"]').send_keys('example')
    driver.find_element_by_xpath('//*[@id="element385"]').send_keys('example')
    driver.find_element_by_xpath('//*[@id="element386"]').send_keys('exmample')