from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query="FRIDGE"
file=0
for i in range(1,20):
    driver.get(f"https://www.amazon.in/s?k={query}&page={i}&crid=39HXJBB0WW82A&sprefix=fridge%2Caps%2C424&ref=nb_sb_noss_2")
    elems = driver.find_elements(By.CLASS_NAME, "puis-card-container")
    print(elems)
    
    for elem in elems:
        d=elem.get_attribute("outerHTML")
# open(path, mode, encoding)  # encoding for text files
        with open(f"Fridge/{query}_{file}.HTML","w",encoding="utf-8") as f:
            f.write(d)  
            file+=1

time.sleep(4)
driver.close()

# print(elem.get_attribute("outerHTML"))
from bs4 import BeautifulSoup
import os
d={'title':[],'price':[],'URL':[]}
quotes={}
for file in os.listdir("Fridge"):
    with open(f"Fridge/{file}") as f:
        html_doc=f.read()
        soup=BeautifulSoup(html_doc,'html.parser')

        # print(title.get_text()) 
        title = soup.find("h2")
        title_text = title.get_text(strip=True) if title else None

        link_tag = soup.find("a", href=True)
        url = "https://www.amazon.in" + link_tag["href"] if link_tag else None

        price_tag = soup.find("span", class_="a-offscreen")
        price = price_tag.get_text(strip=True) if price_tag else None

        d["title"].append(title_text)
        d["price"].append(price)
        d["URL"].append(url)



import pandas as pd
df=pd.DataFrame(d)
df.to_csv("Fridge-Data.csv",index=False,encoding="utf-8")


