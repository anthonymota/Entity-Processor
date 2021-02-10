individual=False
import register_corp
import fbn_san_bernardino
import fbn_la_
import operating_agreement
import register_llc
import infostatement_llc
import re


#get data
your_name = input("Enter your name: ").title()
legal_company_name = input("Legal Company Name (Please include LLC or Inc.): ").title()
date_commenced = input("Date which registrant first commenced business under FBN (MM/DD/YYYY): ")
while not re.match('^\d\d[/]\d\d[/]\d\d\d\d$',date_commenced):
    date_commenced=input("Please enter in the correct format (MM/DD/YYYY): ")
county=input("Which county are you in: ").title()
entity_number= input("Entity Number: ")
organizer_name=input("Organizer Name: ").title()
organizer_email=input("Organizer Email: ")
while not re.match('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',organizer_email):
    organizer_email=input("Please enter a valid email: ")
type_of_business = input("Type of Business: ")
print('Business Address')
business_street = input("Street: ").title()
business_city = input("City: ").title()
business_zip_code = input("Zip: ")
business_state = input('State: ').capitalize()
mailing_address = input(
    'Is mailing address same? ').lower()
while mailing_address!='yes' and mailing_address!='no':
    mailing_address=input("Please enter yes or no: ")
if mailing_address == 'no':
    mailing_street = input("Street: ")
    mailing_city = input("City: ")
    mailing_zip = input("Zipcode: ")
elif mailing_address == 'yes':
    mailing_street = business_street
    mailing_city = business_city
    mailing_zip = business_zip_code
ssn1, ssn2, ssn3 = input("Social Security #: ").replace('-', ' ').split()
card_number = input('Card Number: ')
cvv = input('Security Code: ')
expiration_month = input('Expiration Month(MM): ')
expiration_year = input('Expiration Year(YY): ')
card_name = input('Name on Card: ').title()
phone_number = input('Phone Number: ')
billing_address = input(
    "Is billing address same as business address? ").lower()
while billing_address!='yes' and billing_address!='no':
    billing_address=input("Please enter 'yes' or 'no': ")
if billing_address == 'yes':
    card_street = business_street
    card_city = business_city
    card_zip_code = business_zip_code
    card_state = business_state
elif billing_address == 'no':
    card_street = input('Street: ')
    card_city = input('City: ')
    card_state = input('State: ')
    card_zip_code = input('Zip: ')
print("q\n")
print("\n")
print(
"Your Name:           ",your_name,"\n",
"Legal Company Name: ",legal_company_name,"\n",
"Date Commenced:     ",date_commenced,"\n",
"County:             ",county,"\n",
"Entity Number:      ",entity_number,"\n",
"Organizer Name:     ",organizer_name,"\n",
"Organizer Email:    ",organizer_email,"\n",
"Type of Business:   ",type_of_business,"\n",
"Business Street:    ",business_street,"\n",
"Business City:      ",business_city,"\n",
"Business Zip Code:  ",business_zip_code,"\n",
"Business State:     ",business_state,"\n",
"Mailing Address:    ",mailing_address,"\n",
"Social Security:    ",ssn1, ssn2, ssn3,"\n",
"Card Number:        ",card_number,"\n",
"CVV:                ",cvv,"\n",
"Expiration Month:   ",expiration_month,"\n",
"Expiration Year:    ",expiration_year,"\n",
"Card Name:          ",card_name,"\n",
"Phone Number:       ",phone_number,"\n")


yesorno=input("Is this information correct?").lower()
while yesorno!= 'yes' and yesorno!='no':
    yesorno=input("Please enter 'yes' or 'no': ")
while yesorno=='no':
    edit=input("Which data is incorrect: ").title()
    if edit=="Legal Company Name":
        legal_company_name=input("Legal Company Name (Please include LLC or Inc.): ").title()
        print("You typed: ",legal_company_name)
        while input("Is this correct? ").lower()=="no":
            legal_company_name=input("Legal Company Name (Please include LLC or Inc.): ").title()
            print("You typed: ",legal_company_name)
    elif edit=="Date Commenced":
        date_commenced = input("Date which registrant first commenced business under FBN (MM/DD/YYYY): ")
        while not re.match('^\d\d[/]\d\d[/]\d\d\d\d$',date_commenced):
            date_commenced=input("Please enter in the correct format (MM/DD/YYYY): ")
        print("You typed: ",date_commenced)
        while input("Is this correct? ").lower()=="no":
            date_commenced = input("Date which registrant first commenced business under FBN (MM/DD/YYYY): ")
            while not re.match('^\d\d[/]\d\d[/]\d\d\d\d$',date_commenced):
                date_commenced=input("Please enter in the correct format (MM/DD/YYYY): ")
            print("You typed: ",legal_company_name)
    elif edit=="County":
        county=input("Which county are you in: ").title()
        print("You typed: ",county)
        while input("Is this correct? ").lower()=="no":
            county=input("Which county are you in: ").title()
            print("You typed: ",county)
    elif edit=="Entity Number":
        entity_number= input("Entity Number: ")
        print("You typed: ",entity_number)
        while input("Is this correct? ").lower()=="no":
            entity_number= input("Entity Number: ")
            print("You typed: ",entity_number)
    elif edit=="Organizer Name":
        organizer_name=input("Organizer Name: ").title()
        print("You typed: ",organizer_name)
        while input("Is this correct? ").lower()=="no":
            organizer_name=input("Organizer Name: ").title()
            print("You typed: ",organizer_name)
    elif edit=="Organizer Email":
        organizer_email=input("Organizer Email: ")
        while not re.match('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',organizer_email):
            organizer_email=input("Please enter a valid email: ")
        print("You typed: ",organizer_email)
        while input("Is this correct? ").lower()=="no":
            organizer_email=input("Organizer Email: ")
            while not re.match('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',organizer_email):
                organizer_email=input("Please enter a valid email: ")
            print("You typed: ",organizer_email)
    elif edit=="Type of Business":
        type_of_business = input("Type of Business: ")
        print("You typed: ",type_of_business)
        while input("Is this correct? ").lower()=="no":
            type_of_business = input("Type of Business: ")
            print("You typed: ",type_of_business)
    elif edit=="Business Street":
        business_street = input("Street: ").title()
        print("You typed: ",business_street)
        while input("Is this correct? ").lower()=="no":
            business_street = input("Street: ").title()
            print("You typed: ",business_street)
    elif edit=="Business City":
        business_city = input("City: ").title()
        print("You typed: ",business_city)
        while input("Is this correct? ").lower()=="no":
            business_city = input("City: ").title()
            print("You typed: ",business_city)
    elif edit=="Business Zip Code":
        business_zip_code = input("Zip: ")
        print("You typed: ",business_zip_code)
        while input("Is this correct? ").lower()=="no":
            business_zip_code = input("Zip: ")
            print("You typed: ",business_zip_code)
    elif edit=="Business State":
        business_state = input('State: ').capitalize()
        print("You typed: ",business_state)
        while input("Is this correct? ").lower()=="no":
            business_state = input('State: ').capitalize()
            print("You typed: ",business_state)
    elif edit=="Social Security":
        ssn1, ssn2, ssn3 = input("Social Security #: ").replace('-', ' ').split()
        print("You typed: ",ssn1,ssn2,ssn3)
        while input("Is this correct? ").lower()=="no":
            ssn1, ssn2, ssn3 = input("Social Security #: ").replace('-', ' ').split()
            print("You typed: ",ssn1,ssn2,ssn3)
    elif edit=="Card Number":
        card_number = input('Card Number: ')
        print("You typed: ",card_number)
        while input("Is this correct? ").lower()=="no":
            card_number = input('Card Number: ')
            print("You typed: ",card_number)
    elif edit=="Cvv":
        cvv = input('Security Code: ')
        print("You typed: ",cvv)
        while input("Is this correct? ").lower()=="no":
            cvv = input('Security Code: ')
            print("You typed: ",cvv)
    elif edit=="Expiration Month":
        expiration_month = input('Expiration Month(MM): ')
        print("You typed: ",expiration_month)
        while input("Is this correct? ").lower()=="no":
            expiration_month = input('Expiration Month(MM): ')
            print("You typed: ",expiration_month)
    elif edit=="Expiration Year":
        expiration_year = input('Expiration Year(YY): ')
        print("You typed: ",expiration_year)
        while input("Is this correct? ").lower()=="no":
            expiration_year = input('Expiration Year(YY): ')
            print("You typed: ",expiration_year)
    elif edit=="Card Name":
        card_name = input('Name on Card: ').title()
        print("You typed: ",card_name)
        while input("Is this correct? ").lower()=="no":
            card_name = input('Name on Card: ').title()
            print("You typed: ",card_name)
    elif edit=="Phone Number":
        phone_number = input('Phone Number: ')
        print("You typed: ",phone_number)
        while input("Is this correct? ").lower()=="no":
            phone_number = input('Phone Number: ')
            print("You typed: ",phone_number)
    yesorno=input("Is everything correct now? ").lower()
    while yesorno!= 'yes' and yesorno!='no':
        yesorno=input("Please enter 'yes' or 'no': ")

if 'Inc' in legal_company_name:
    register_corp.run(legal_company_name,business_street,business_city,business_zip_code)
    if 'San Bernardino' in county:
        fbn_san_bernardino.run(legal_company_name,county,business_street,business_city,business_zip_code,business_state,phone_number,your_name,date_commenced)
    else:          lalala
        fbn_la_.run(legal_company_name,business_street,business_city,business_zip_code,organizer_name)
elif 'Llc' in legal_company_name:
    print('Its an LLC!')
    register_llc.run(legal_company_name,business_street,business_city,business_state,business_zip_code,mailing_address,mailing_street,mailing_city,mailing_zip,organizer_name,organizer_email,expiration_month,expiration_year,card_name,card_number,cvv,card_street,card_city,card_state,card_zip_code,phone_number)
    if 'San Bernardino' in county:
        fbn_san_bernardino.run(legal_company_name,county,business_street,business_city,business_zip_code,business_state,phone_number,your_name,date_commenced)
    else:
        fbn_la_.run(legal_company_name,business_street,business_city,business_zip_code,organizer_name)
    infostatement_llc.run(entity_number,business_street,business_city,business_zip_code,owner_first_name,owner_last_name,type_of_business,organizer_email)
    operating_agreement.run(owner_last_name,owner_first_name,wife_last_name,wife_name,company_name,aog_date,business_street,business_city,business_zip_code,business_state,type_of_business)
else:
    individual=True
    if 'San Bernardino' in county:
        fbn_san_bernardino.run(legal_company_name,county,business_street,business_city,business_zip_code,business_state,phone_number,your_name,date_commenced)
    else:
        fbn_la_.run(company_name,business_street,business_city,business_zip_code,organizer_name)
    operating_agreement.run(owner_last_name,owner_first_name,wife_last_name,wife_name,company_name,aog_date,business_street,business_city,business_zip_code,business_state,type_of_business)
    
