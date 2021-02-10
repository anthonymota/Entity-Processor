individual=False
import register_corp
import fbn_san_bernardino
import fbn_la_
import operating_agreement
import register_llc
import infostatement_llc
from docx import Document
from docx.shared import Inches
import subprocess


variables={}
document = Document('data_document.docx')
for k in document.paragraphs:
    for j in range(len(k.text)):
        if k.text[j]==':':
            variables[k.text[:j]]=k.text[j+2:]

if 'Inc' in variables["legal_company_name"]:
    register_corp.run(variables["legal_company_name"],variables["business_street"],variables["business_city"],variables["business_zip_code"])
    if 'San Bernardino' in variables['county']:
        fbn_san_bernardino.run(variables["legal_company_name"],variables["county"],variables["business_street"],variables["business_city"],variables["business_zip_code"],variables["business_state"],variables["phone_number"],variables["your_name"],variables["date_commenced"])
    else:        
        fbn_la_.run(variables["legal_company_name"],variables["business_street"],variables["business_city"],variables["business_zip_code"],variables["organizer_name"])
elif 'Llc' in variables["legal_company_name"]:
    print('Its an LLC!')
    register_llc.run(variables["legal_company_name"],variables["business_street"],variables["business_city"],variables["business_state"],variables["business_zip_code"],variables["mailing_address"],variables["mailing_street"],variables["mailing_city"],variables["mailing_zip_code"],variables["organizer_name"],variables["organizer_email"],variables["expiration_month"],variables["expiration_year"],variables["card_name"],variables["card_number"],variables["cvv"],variables["card_street"],variables["card_city"],variables["card_state"],variables["card_zip_code"],variables["phone_number"])
    if 'San Bernardino' in variables["county"]:
        fbn_san_bernardino.run(variables["legal_company_name"],variables["county"],variables["business_street"],variables["business_city"],variables["business_zip_code"],variables["business_state"],variables["phone_number"],variables["your_name"],variables["date_commenced"])
    else:
        fbn_la_.run(variables["legal_company_name"],variables["business_street"],variables["business_city"],variables["business_zip_code"],variables["organizer_name"])
    infostatement_llc.run(entity_number,variables["business_street"],variables["business_city"],variables["business_zip_code"],owner_first_name,owner_last_name,type_of_business,variables["organizer_email"])
    operating_agreement.run(owner_last_name,owner_first_name,wife_last_name,wife_name,company_name,aog_date,variables["business_street"],variables["business_city"],variables["business_zip_code"],variables["business_state"],type_of_business)
else:
    individual=True
    if 'San Bernardino' in variables["county"]:
        fbn_san_bernardino.run(variables["legal_company_name"],variables["county"],variables["business_street"],variables["business_city"],variables["business_zip_code"],variables["business_state"],variables["phone_number"],your_name,date_commenced)
    else:
        fbn_la_.run(company_name,variables["business_street"],variables["business_city"],variables["business_zip_code"],variables["organizer_name"])
    operating_agreement.run(owner_last_name,owner_first_name,wife_last_name,wife_name,company_name,aog_date,variables["business_street"],variables["business_city"],variables["business_zip_code"],variables["business_state"],type_of_business)
    
