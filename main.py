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
            if k.text[j+1]==" ":
                variables[k.text[:j]]=k.text[j+2:]
            else:
                variables[k.text[:j]]=k.text[j+1:]
    if 'mailing address' in k.text:
        for a in range(len(k.text)):
            if k.text[a]==':':
                if k.text[a+1]==" ":
                    mailing_address=k.text[a+2:]
                else:
                    mailing_address=k.text[a+1:]
                break

if mailing_address=='yes':
    variables.update({'mailing_street':variables['business_street']})
    variables.update({'mailing_city':variables['business_city']})
    variables.update({'mailing_zip_code':variables['business_zip_code']})
print('\n')
print(variables)
if 'Inc' in variables["legal_company_name"]:
    register_corp.run(variables["legal_company_name"],variables["business_street"],variables["business_city"],variables["business_zip_code"],mailing_address)
    if 'San Bernardino' in variables['county']:
        fbn_san_bernardino.run(variables["legal_company_name"],variables["county"],variables["business_street"],variables["business_city"],variables["business_zip_code"],variables["business_state"],variables["phone_number"],variables["your_name"],variables["date_commenced"])
    else:        
        fbn_la_.run(variables["legal_company_name"],variables["business_street"],variables["business_city"],variables["business_zip_code"],variables["organizer_name"])
elif 'Llc' in variables["legal_company_name"]:
    print('Its an LLC!')
    register_llc.run(variables["legal_company_name"],variables["business_street"],variables["business_city"],variables["business_state"],variables["business_zip_code"],mailing_address,variables["mailing_street"],variables["mailing_city"],variables["mailing_zip_code"],variables["organizer_name"],variables["organizer_email"],variables["expiration_month"],variables["expiration_year"],variables["card_name"],variables["card_number"],variables["cvv"],variables["card_street"],variables["card_city"],variables["card_state"],variables["card_zip_code"],variables["phone_number"])
    if 'San Bernardino' in variables["county"]:
        fbn_san_bernardino.run(variables["legal_company_name"],variables["county"],variables["business_street"],variables["business_city"],variables["business_zip_code"],variables["business_state"],variables["phone_number"],variables["your_name"],variables["date_commenced"])
    else:
        fbn_la_.run(variables["legal_company_name"],variables["business_street"],variables["business_city"],variables["business_zip_code"],variables["organizer_name"])
    infostatement_llc.run(variables["entity_number"],variables["business_street"],variables["business_city"],variables["business_zip_code"],owner_first_name,owner_last_name,variables["type_of_business"],variables["organizer_email"])
    operating_agreement.run(owner_last_name,owner_first_name,wife_last_name,wife_name,company_name,aog_date,variables["business_street"],variables["business_city"],variables["business_zip_code"],variables["business_state"],variables["type_of_business"])
else:
    individual=True
    if 'San Bernardino' in variables["county"]:
        fbn_san_bernardino.run(variables["legal_company_name"],variables["county"],variables["business_street"],variables["business_city"],variables["business_zip_code"],variables["business_state"],variables["phone_number"],variables["your_name"],variables["date_commenced"])
    else:
        fbn_la_.run(variables["legal_company_name"],variables["business_street"],variables["business_city"],variables["business_zip_code"],variables["organizer_name"])
    operating_agreement.run(owner_last_name,owner_first_name,wife_last_name,wife_name,variables["legal_company_name"],aog_date,variables["business_street"],variables["business_city"],variables["business_zip_code"],variables["business_state"],variables["type_of_business"])
    
