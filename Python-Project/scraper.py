from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#open saved list
print("It's running")
df = pd.read_csv("NYC.csv")

#store url && title into list
list_link = df["URL"]
list_title = df["Title"]

print(list_link)
driver = webdriver.Firefox()
print("opening driver")
category = ''
title = ''
page_num = 1
categories = []
titles = []
res = []

# Navigate to Url
# Problem to solve : it can't read 'hotel link. why?? -> because it doesn't have classname DkEaL.
# Problem to solve : store title and category in Pair
index = 0

for l in list_link:
    try:
           driver.get(l)
           if page_num == 1:
                driver.implicitly_wait(10) 
                category = driver.find_element(By.CLASS_NAME, 'DkEaL ')
           else:
               time.sleep(2)
    except:
        pass
    
#problem : it can't retreive category.text --> error ---> solved
#problem : get NAME of the place and store it into list --> solved
    if category:
        try:
            categories += [category.text]
            res.append((category.text, list_title[index]))
            
        except:
            print("ERROR: No category")
            pass
    else:
        pass
    
    index += 1
    page_num =+ 1

print(res)

userInput = input("Which category you want to see?")

result = []
for i in res:
    #i[0] == category
    #i[1] == name of the place
    if lower(i[0]) == lower(userInput):
        result.append(i[1])

print(result)
