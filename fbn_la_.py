from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
from selenium.webdriver.chrome.options import Options

def run(legal_company_name,business_street,business_city,business_zip_code,organizer_name):
    # initiate driver
    chrome_options = Options()
    chrome_options.add_experimental_option("detach", True)
    driver = webdriver.Chrome(ChromeDriverManager().install(), chrome_options=chrome_options)
    driver.get('https://apps.lavote.net/OBFR/BFRMain.aspx')

    #begin forms
    driver.find_element_by_xpath('//*[@id="cphContent_btnThirdParty"]').click()
    driver.find_element_by_xpath('//*[@id="cphContent_btnFBN_Original"]').click()
    driver.find_element_by_xpath('//*[@id="cphContent_fbnOriginalWizard_chkValidFBN"]').click()
    driver.find_element_by_xpath('//*[@id="cphContent_fbnOriginalWizard_StartNavigationTemplateContainerID_StepStartButton"]').click()

    #business name
    driver.find_element_by_xpath('//*[@id="cphContent_fbnOriginalWizard_txtStep1AddBusinessName"]').send_keys(legal_company_name)
    driver.find_element_by_xpath('//*[@id="cphContent_fbnOriginalWizard_btnStep1AddBusinessName"]').click()
    driver.find_element_by_xpath('//*[@id="cphContent_fbnOriginalWizard_StepNavigationTemplateContainerID_StepNextButton"]').click()

    #business address
    driver.find_element_by_xpath('//*[@id="cphContent_fbnOriginalWizard_txtStep2BusinessAddress"]').send_keys(business_street)
    driver.find_element_by_xpath('//*[@id="cphContent_fbnOriginalWizard_txtBusinessCityList"]').send_keys(business_city)
    driver.find_element_by_xpath('//*[@id="cphContent_fbnOriginalWizard_txtStep2BusinessZipCode"]').send_keys(business_zip_code)
    driver.find_element_by_xpath('//*[@id="cphContent_fbnOriginalWizard_StepNavigationTemplateContainerID_StepNextButton"]').click()

    #registered owner
    driver.find_element_by_xpath('//*[@id="cphContent_fbnOriginalWizard_txtStep3OwnerName"]').send_keys(organizer_name)
    driver.find_element_by_xpath('//*[@id="cphContent_fbnOriginalWizard_txtStep3OwnerAddress"]').send_keys(business_street)
    driver.find_element_by_xpath('//*[@id="cphContent_fbnOriginalWizard_txtStep3OwnerCity"]').send_keys(business_city)
    driver.find_element_by_xpath('//*[@id="cphContent_fbnOriginalWizard_txtStep3OwnerZipCode"]').send_keys(business_zip_code)
    driver.find_element_by_xpath('//*[@id="cphContent_fbnOriginalWizard_btnStep3AddOwner"]').click()
    driver.find_element_by_xpath('//*[@id="cphContent_fbnOriginalWizard_StepNavigationTemplateContainerID_StepNextButton"]').click()

    #signature
    r_owner=Select(driver.find_element_by_xpath('//*[@id="cphContent_fbnOriginalWizard_ddlStep4SelectOwnerName"]'))
    r_owner.select_by_value(organizer_name.upper())
    title=Select(driver.find_element_by_xpath('//*[@id="cphContent_fbnOriginalWizard_ddlStep4SignatoryTitle"]'))
    title.select_by_value('CEO')
    driver.find_element_by_xpath('//*[@id="cphContent_fbnOriginalWizard_StepNavigationTemplateContainerID_StepNextButton"]').click()

    #additional info
    r=Select(driver.find_element_by_xpath('//*[@id="cphContent_fbnOriginalWizard_ddlStep5BusinessType"]'))
    r.select_by_index('4')
    driver.find_element_by_xpath('//*[@id="cphContent_fbnOriginalWizard_txtStep5CommenceTS"]').send_keys('N/A')
    driver.find_element_by_xpath('//*[@id="cphContent_fbnOriginalWizard_StepNavigationTemplateContainerID_StepNextButton"]').click()

    #preview


