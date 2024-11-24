import docx

document = docx.Document('IT_Sample_Resume.docx') #assigns the document referenced to the document variable

#for loop that will search the document for key words
for para in document.paragraphs:
    if 'python' in para.text.lower(): #checks for the word python
        print('A python programmer!') #if present prints this string
    # print(para.text)