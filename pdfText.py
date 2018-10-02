import PyPDF2 
# import textract
# from nltk.tokenize import word_tokenize
# from nltk.corpus import stopwords


fileName =  "/home/sharang/Downloads/sample-invoice.pdf"
pdfFileObj = open(fileName,'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
num_pages = pdfReader.numPages
count = 0
text = ""
while count < num_pages:
    pageObj = pdfReader.getPage(count)
    count +=1
    text += pageObj.extractText()

print(text)

# tokens = word_tokenize(text)
# print(tokens)

# # punctuations = ['(',')',';',':','[',']',',']

# keywords = [word for word in tokens if not word in stop_words and not word in punctuations]
# print(keywords)



