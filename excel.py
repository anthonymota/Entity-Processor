import xlsxwriter

company = 'la senda2'


workbook = xlsxwriter.Workbook(company+'.xlsx')
worksheet = workbook.add_worksheet()
underline = workbook.add_format({'underline': True})
bold = workbook.add_format({'bold': True})

worksheet.write('A1', 'Hello World', underline)

workbook.close()
