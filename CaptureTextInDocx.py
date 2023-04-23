import docx
import time
from docx import Document

log=open('log.txt', mode='a', encoding='utf-8')

for i in range(1,38):
    filename="G:\LOST DIR\\第二轮\\o\\word\\text ("+str(i)+").docx"
    file=docx.Document(filename)
    for para in file.paragraphs:
        print(para.text, file=log)
    print("Success in"+filename)
