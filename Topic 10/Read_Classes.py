import openpyxl

workbook = openpyxl.load_workbook('ITEC_Courses.xlsx') #loads excell file into python

sheet_names = workbook.sheetnames #assign variable to identify sheet names in excell file
print(sheet_names)

codes_sheet = workbook.active #active assigns first sheet to variable


b2_data = codes_sheet['B2'].value #retreives the data from the B2 cell
print(b2_data)

c5_data = codes_sheet['C5'].value
print(c5_data)

for row in codes_sheet.rows: #prints all the rows in order
    for cell in row:
        print(cell.value)
print()

for col in codes_sheet.columns: #prints all columns in order
    for cell in col:
        print(cell.value)

class_names_columns = codes_sheet['C'] #prints data in column c
for cell in class_names_columns:
    print(cell.value)

rooms_sheet = workbook['rooms'] #assigns rooms sheet to variable
rooms_column = rooms_sheet['B'] #prints data in column b
for cell in rooms_column:
    print(cell.value)