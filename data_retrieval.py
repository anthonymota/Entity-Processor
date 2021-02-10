from docx import Document
from docx.shared import Inches
import subprocess


variables={}
document = Document('data_document.docx')
for k in document.paragraphs:
    for j in range(len(k.text)):
        if k.text[j]==':':
            variables[k.text[:j]]=k.text[j+2:]

print(variables)


document.save('finished_data.docx')