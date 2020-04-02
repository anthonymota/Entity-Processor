from pdfrw import PdfReader
import pdb

print('\n')

template = PdfReader('f2553.pdf')

if template.isEncrypted:
    print('true')