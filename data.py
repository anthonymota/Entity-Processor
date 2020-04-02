# get data
owner_first_name = input("Business Owner First Name: ")
owner_last_name = input("Business Owner Last Name: ")
ssn1, ssn2, ssn3 = input("Social Security #: ").replace('-', ' ').split()
company_name = input("Company name: ")
company_name = " ".join(w.capitalize() for w in company_name.split())
print('Business Address')
business_street = input("Street: ").title()
business_city = input("City: ").title()
business_zip_code = input("Zip: ")
business_state = input('State: ').capitalize()
mailing_address = input(
    'Is mailing address same? ').lower()
if mailing_address == 'no':
    mailing_street = input("Street: ")
    mailing_city = input("City: ")
    mailing_zip = input("Zipcode: ")
elif mailing_address == 'yes':
    mailing_street = business_street
    mailing_city = business_city
    mailing_zip = business_zip_code
first_name, last_name = input("Organizer Name: ").title().split()
organizer_name = first_name + " " + last_name
organizer_email = input('Organizer Email: ')
card_number = input('Card Number: ')
cvv = input('Security Code: ')
expiration_month = input('Expiration Month(MM): ')
expiration_year = input('Expiration Year(YY): ')
card_name = input('Name on Card: ').title()
phone_number = input('Phone Number: ')
billing_address = input(
    "Is billing address same as business address? ").lower()
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
