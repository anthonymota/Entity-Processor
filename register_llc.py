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


def run(legal_company_name,business_street,business_city,business_state,business_zip_code,mailing_address,mailing_street,mailing_city,mailing_zip,organizer_name,organizer_email,expiration_month,expiration_year,card_name,card_number,cvv,card_street,card_city,card_state,card_zip_code,phone_number):

    
    print('\n')
    print('\n')

    # initiate driver
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    driver.get('https://llcbizfile.sos.ca.gov/registration/submission/new')
    driver.switch_to.frame(0)


    # begin form

    driver.find_element_by_xpath(
        '/html/body/div[8]/div/div[2]/div/div/div[1]/div[1]/div/div/div/div/form/div/div[2]/div[4]/div/div[2]/input').send_keys(legal_company_name)

    llc_type = Select(driver.find_element_by_id('element89'))
    llc_type.select_by_index("2")

    time.sleep(1)

    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.NAME, "element2"))).click()

    # form2
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'element130'))).send_keys(business_street)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'element125'))).send_keys(business_city)
    WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'element129'))).send_keys(business_zip_code)
    if mailing_address == 'yes':
        WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, 'element86_Yes'))).click()
    elif mailing_address == 'no':
        driver.find_element_by_xpath('//*[@id="element86_No"]').click()
        country = Select(driver.find_element_by_xpath('//*[@id="element348"]'))
        country.select_by_index('1')
        driver.find_element_by_xpath(
            '//*[@id="element26"]').send_keys(mailing_street)
        driver.find_element_by_xpath(
            '//*[@id="element25"]').send_keys(mailing_city)
        new_state = Select(driver.find_element_by_xpath('//*[@id="element349"]'))
        new_state.select_by_index(5)
        driver.find_element_by_xpath('//*[@id="element24"]').send_keys(mailing_zip)

    driver.find_element_by_xpath(
        '//*[@id="form-section-1"]/div[19]/input[2]').click()

    # form3
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="element78_corp"]').click()
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="s2id_element168"]/span[1]/span').click()
    driver.find_element_by_xpath(
        '/html/body/span/span/span[1]/input').send_keys('la senda')
    time.sleep(2)
    driver.find_element_by_xpath(
        '//*[@id="select2-element168-results"]/li').click()
    driver.find_element_by_xpath(
        '//*[@id="form-section-2"]/div[19]/input[2]').click()

    # form4
    driver.find_element_by_xpath('//*[@id="element43_OneManager"]').click()
    driver.find_element_by_xpath(
        '//*[@id="form-section-3"]/div[4]/input[2]').click()

    # form5
    driver.find_element_by_xpath(
        '//*[@id="element83"]').send_keys(organizer_name)
    driver.find_element_by_xpath(
        '//*[@id="element47"]').send_keys(organizer_email)
    driver.find_element_by_xpath(
        '//*[@id="element338"]').send_keys(organizer_email)
    driver.find_element_by_xpath('//*[@id="element352_Option_1"]').click()
    driver.find_element_by_xpath(
        '//*[@id="form-section-4"]/div[15]/input[2]').click()
    time.sleep(1)
    driver.find_element_by_xpath(
        '//*[@id="form-section-5"]/div[13]/input[2]').click()

    # form6
    product = Select(driver.find_element_by_xpath('//*[@id="element260"]'))
    product.select_by_index('2')
    driver.find_element_by_xpath('//*[@id="element91"]').send_keys(card_number)
    driver.find_element_by_xpath('//*[@id="element94"]').send_keys(cvv)
    driver.find_element_by_xpath(
        '//*[@id="element325"]').send_keys(expiration_month)
    driver.find_element_by_xpath(
        '//*[@id="element326"]').send_keys(expiration_year)
    driver.find_element_by_xpath('//*[@id="element93"]').send_keys(card_name)
    driver.find_element_by_xpath('//*[@id="element161"]').send_keys(card_street)
    driver.find_element_by_xpath('//*[@id="element162"]').send_keys(card_city)
    driver.find_element_by_xpath('//*[@id="element164"]').send_keys(card_state)
    driver.find_element_by_xpath('//*[@id="element163"]').send_keys(card_zip_code)
    driver.find_element_by_xpath('//*[@id="element165"]').click()
    driver.find_element_by_xpath('//*[@id="element165"]').send_keys(phone_number)


    # begin EIN Form


    # create excel file
    workbook = xlsxwriter.Workbook(legal_company_name+'.xlsx')
    worksheet = workbook.add_worksheet()

    # declare formats
    underline = workbook.add_format({"underline": True})
    bold = workbook.add_format({"bold": True})

    # write data to excel file
    worksheet.write
    worksheet.write('A1', "Company Name:", bold)
    worksheet.write('B1', legal_company_name)
    worksheet.write('A3', "Business Address", underline)
    worksheet.write('A4', "Street:", bold)
    worksheet.write('B4', business_street)
    worksheet.write('A5', "City:", bold)
    worksheet.write('B5', business_city)
    worksheet.write('A6', "State", bold)
    worksheet.write('B6', business_state)
    worksheet.write('A7', 'Zip Code:', bold)
    worksheet.write('B7', business_zip_code)
    worksheet.write('A9', "Mailing Address", underline)
    worksheet.write('A10', "Street:", bold)
    worksheet.write('B10', mailing_street)
    worksheet.write('A11', "City:", bold)
    worksheet.write('B11', mailing_city)
    worksheet.write('A12', "Zip Code:", bold)
    worksheet.write('B12', mailing_zip)
    worksheet.write('A14', "Organizer Name:", bold)
    worksheet.write('B14', organizer_name)
    worksheet.write('A15', "Organizer Email:", bold)
    worksheet.write('B15', organizer_email)
    worksheet.write('A17', "Name on Card:")
    worksheet.write('B17', card_name)
    worksheet.write('A18', "Card Number:")
    worksheet.write('B18', card_number)
    worksheet.write('A19', "Security Code:")
    worksheet.write('B19', cvv)
    worksheet.write('A20', "Expiration Month:")
    worksheet.write('B20', expiration_month)
    worksheet.write('A21', "Expiration Year:")
    worksheet.write('B21', expiration_year)
    worksheet.write('A22', "Phone Number:")
    worksheet.write('B22', phone_number)


    workbook.close()
