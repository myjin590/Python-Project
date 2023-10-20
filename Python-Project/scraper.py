from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import numpy as np
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

#open saved list
df = pd.read_csv("NYC.csv")

#store url into list_link
list_link = df["URL"]
#print(list_link)

driver = webdriver.Firefox()
category = ''
page_num = 1
categories = []
# Navigate to Url
# Problem to solve : it can't read hotel link! why?? -> because it doesn't have classname DkEaL.
for l in list_link:
    print("start loop")
    try:
           driver.get(l)
           if page_num == 1:
                driver.implicitly_wait(10) 
                #element = WebDriverWait(driver, 50).until(EC.presence_of_element_located((By.XPATH, "//*[contains(text(), 'Coffee')]")))

                #my_element = driver.find_elements_by_xpath("//span[text()='hotel']")
                category = driver.find_element(By.CLASS_NAME, 'DkEaL ')
           else:
               time.sleep(2)

    except NoSuchElementException:
        print("No such element")
    
    finally:
        if(category != ''):
            categories += category.text
        else:
            driver.refresh()
    page_num =+ 1
        

print(categories)
#get category
#print(category.text)

