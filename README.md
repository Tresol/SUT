# SUT: A Short Description
SUT refers to the repository called Some Useful Tools, which stores some useful tools I have used in my computer.

I hope the tools in the repository will help you. Also, it will be appreciated if you fork and star my repository.

## Notification

The repository SUT of Tresol is licensed under the GPL 3.0 License. Please follow the license and contribute to the Open-Source community together.

## Report

If you find something incorrect or illegal in my repository, please report it to me.

My email is <tresol@163.com>.

### Guide for this tool 

#### Environment

Python 3.7+.

The tool is tested in Python 3.11, Windows 10 22H2 Professional.

#### Target Function

I develop the tool to read and output the content in a series of `docx` files.

#### Explanation

The `docx` is a format that matches the Open XML Standard, which was created by the Microsoft Cooperation.

Different from the old format `doc` , the `docx` file is composed of the XML file which contains the content of the `docx` file and other audio media, like pictures, audios, etc. which are referred in the file.

As a result, we can fetch the content of the `docx` file easily by reading the content of the XML file. This is also the reason why we can't read `doc` files using the tool. 

#### Code

The following is the basic code.

```python
import docx
from docx import Document

log=open('result.txt', mode='a', encoding='utf-8')

filename="yourfilename.docx"
file=docx.Document(filename)
for para in file.paragraphs:
    print(para.text, file=result)
```

#### Notes

1. You should install the `python-docx` package before running the code, using the order `pip install python-docx` in Command Prompt. However, you should write `include docx` in the code instead of ` include python-docx`.
2. You cannot process `doc` file using this tool.
