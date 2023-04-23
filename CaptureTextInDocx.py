import docx
# Please install python-docx package first using the command "pip install python-docx".
# import time
from docx import Document

result=open('result.txt', mode='a', encoding='utf-8')

filename="G:\LOST DIR"+str(i)+").docx"
file=docx.Document(filename)
for para in file.paragraphs:
    print(para.text, file=log)
