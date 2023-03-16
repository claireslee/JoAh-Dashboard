#importing required modules
import PyPDF2

def subtract(num1, num2):
    return num1 - num2

# creating a pdf file object
pdfFileObj = open('Hello world!.pdf', 'rb')

# creating a pdf reader object
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# printing number of pages in pdf file
print(pdfReader.numPages)

# creating a page object
pageObj = pdfReader.getPage(0)
  
# extracting text from page
print(pageObj.extractText())
  
# closing the pdf file object
pdfFileObj.close()

