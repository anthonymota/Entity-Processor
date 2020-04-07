from docx import Document
import re
from data2 import *


def docx_replace_regex(doc_obj, regex , replace):
        for p in doc_obj.paragraphs:
            if regex.search(p.text):
                inline = p.runs
                # Loop added to work with runs (strings with same style)
                for i in range(len(inline)):
                    if regex.search(inline[i].text):
                        text = regex.sub(replace, inline[i].text)
                        inline[i].text = text   


regex1 = re.compile(r"first_name")
replace1 = owner_first_name
regex2 = re.compile(r"last")
replace2 = owner_last_name
regex3 = re.compile(r"fn")
replace3 = wife_name
regex4 = re.compile(r"second_name")
replace4 = wife_last_name
regex5 = re.compile(r"company_name")
replace5 = company_name
regex6 = re.compile(r"aog_date")
replace6 = aog_date
regex7 = re.compile(r"business_street")
replace7 = business_street
regex8 = re.compile(r"business_city")
replace8 = business_city
regex9 = re.compile(r"paraca")
replace9 = business_state
regex10 = re.compile(r"business_zip_code")
replace10 = business_zip_code
regex11 = re.compile(r"business_type")
replace11 = type_of_business

filename = "OPERATING AGREEMENT.docx"
doc = Document(filename)
docx_replace_regex(doc, regex1 , replace1)
docx_replace_regex(doc, regex2 , replace2)
docx_replace_regex(doc, regex3 , replace3)
docx_replace_regex(doc, regex4, replace4)
docx_replace_regex(doc, regex5, replace5)
docx_replace_regex(doc, regex6, replace6)
docx_replace_regex(doc, regex7 , replace7)
docx_replace_regex(doc, regex8 , replace8)
docx_replace_regex(doc, regex9 , replace9)
docx_replace_regex(doc, regex10 , replace10)
docx_replace_regex(doc, regex11 , replace11)
doc.save('OPERATING AGREEMENT2.docx')
