from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver.chrome.options import Options


def run(legal_company_name,county,business_street,business_city,business_zip_code,business_state,phone_number,your_name,date_commenced):
    print('\n')
    print("PROGRAM STARTING")
    print('~~~~~~')
    print('\n')
    # initiate driver
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    driver.get('http://arcselfservice.sbcounty.gov/web/user/disclaimer')

    #begin
    driver.find_element_by_xpath('//*[@id="submitDisclaimerAccept"]').click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div/div[3]/div[2]/div/div/div[2]/a[1]"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div/div[3]/div[2]/a[2]"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div/div[3]/div[2]/a"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[8]/div[1]/div/a[1]"))).click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div/form/sl/li[2]/fieldset/div/div[1]/div[1]/input"))).send_keys(legal_company_name)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div/form/sl/li[2]/fieldset/div/div[1]/div[2]/input"))).send_keys(county)
    driver.find_element_by_xpath('/html/body/div[2]/div[8]/div[1]/div/a[1]').click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div/form/div[1]/div[1]/div/div/div/div/div[1]/div/input"))).send_keys(business_street)
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/form/div[1]/div[1]/div/div/div/div/div[3]/div/input').send_keys(business_city)
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/form/div[1]/div[1]/div/div/div/div/div[4]/div/input').send_keys(business_state)
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/form/div[1]/div[1]/div/div/div/div/div[5]/div/input').send_keys(business_zip_code)
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/form/div[2]/div/div/div/input').send_keys(phone_number)
    driver.find_element_by_xpath('/html/body/div[2]/div[8]/div[1]/div/a[1]').click()
    driver.implicitly_wait(5)
    c=Select(driver.find_element_by_xpath("/html/body/div[2]/div[2]/div/form/div/div/div/div[1]/div/select"))
    c.select_by_visible_text("Individual")
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/form/div/div/div/div[2]/input').send_keys(date_commenced)
    driver.find_element_by_xpath('/html/body/div[2]/div[8]/div[1]/div/a[1]').click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div/form/sl/li[2]/fieldset/div/div[1]/div[1]/div[1]/div/div/input"))).send_keys(legal_company_name)
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/form/sl/li[2]/fieldset/div/div[1]/div[2]/div/div/div[1]/div[1]/div/input').send_keys(business_street)
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/form/sl/li[2]/fieldset/div/div[1]/div[2]/div/div/div[1]/div[3]/div/input').send_keys(business_city)
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/form/sl/li[2]/fieldset/div/div[1]/div[2]/div/div/div[1]/div[4]/div/input').send_keys(business_state)
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/form/sl/li[2]/fieldset/div/div[1]/div[2]/div/div/div[1]/div[5]/div/input').send_keys(business_zip_code)
    driver.find_element_by_xpath('/html/body/div[2]/div[8]/div[1]/div/a[1]').click()
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[2]/div[2]/div/form/div/div[1]/div/div/input"))).send_keys(your_name)
    driver.find_element_by_xpath('/html/body/div[2]/div[8]/div[1]/div/a[1]').click()
    print('hello')