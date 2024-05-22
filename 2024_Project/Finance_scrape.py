from pypdf import PdfReader 
import re

# creating a pdf reader object 
reader = PdfReader('Statement.pdf') 
  
# printing number of pages in pdf file 
print(len(reader.pages)) 
  
# getting a specific page from the pdf file 
trans = []

transNo = 0
transDate = ""
postDate = ""
details = ""
amount = 0
i =0

    
def getTransNo(text, page):
    if(page == 0):
        #start
        x = text.find("001") #400 - 402 => 001
            #403 => whitespace
        global transNo 
        transNo = int(text[x] + text[x+1] + text[x+2])
        print(transNo)
        #return index number of M == 404
        #return index text[x+4]
        return x+4
    else:
        return 0

def getTransDate(text, index):
    print("Getting Trans Date...")
    dateStr=""
    for i in range(index, index+6):
        dateStr += text[i]
    print(dateStr) 
    return index + 7

def getPostDate(text, index):
    print("Getting Post Date...")
    dateStr=""
    for i in range(index, index+6):
        dateStr += text[i]
    print(dateStr) 
    return index + 7

def getDetails(text, index):
    print("Getting details...")
    detailStr=""
    substr = ""
    #typecast next Trans No to string to find the index of current TransNo's price

    nextTransNo = transNo+1
    print("Next Trans No is --> ")
    print(transNo)
    if nextTransNo < 10 :
        substr = "00" + str(nextTransNo)
    elif nextTransNo > 9 :
        substr = "0" + str(nextTransNo)
    elif nextTransNo > 99 :
        substr = str(nextTransNo)
    
    nextTransNoIndex = text.find(substr) 
    x = text[index:nextTransNoIndex]
    strArray = x.split()
    print(strArray) #last element in array will be always price!
    details = ""
    for i in range(len(strArray)-1):
        details += strArray[i]
        details += " "
    print(details)
    print("Price-->")
    print(strArray[len(strArray)-1])



for p in reader.pages:
    print("page no : " + str(i+1)) # because i == 0, we want to print starting 1
    text = p.extract_text() #big string?
    # print(text)
    print("Transaction number")
    if(i == 0):
        nextIndex = getTransNo(text, i) #params: text, page number
        print("After getTransNo, next Index --> ")
        print(nextIndex)
        if(nextIndex != 0):
            nextIndex = getTransDate(text, nextIndex)
            print("After getTransNo, next Index --> ")
            print(nextIndex)
            nextIndex = getPostDate(text, nextIndex)
            getDetails(text,nextIndex)
        else:
            print("nextIndex is 0, error")
        

        #get next string after amount
    i+= 1


# extracting text from page 
