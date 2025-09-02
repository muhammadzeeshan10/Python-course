from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
query=["books"]
file=0
for i in range(1,10):
    driver.get(f"https://www.daraz.pk/catalog/?page={i}&{query}spm=a2a0e.tm80335142.search.d_go&q=books")
    elems = driver.find_elements(By.CLASS_NAME,"Bm3ON")
    for elem in elems:
        d=elem.get_attribute("outerHTML")
        with open(f"Daraz/{query}_{file}.HTML","w",encoding="utf-8") as f:
            f.write(d)
            file+=1
    print(elem.text)

time.sleep(4)
driver.close()
from bs4 import BeautifulSoup
import os
d={'Title':[],'IMG-URL':[],'price':[]}
quotes={}

for file in os.listdir("Daraz"):
    with open(f"Daraz/{file}",encoding="utf-8") as f:
        html=f.read()
        soup=BeautifulSoup(html,'html.parser')

        # title = soup.find("div", class_="title--wFj93")
        # title_text = title.get_text(strip=True) if title else None
        img = soup.find("img")
        title_text = img["alt"].strip() if img and img.has_attr("alt") else None


        img = soup.find("img")
        img_url = img["src"] if img and img.has_attr("src") else None


        price=soup.find("span",class_="ooOxS")
        price_link=price.get_text() if price else None
        
        
        d["Title"].append(title_text)     
        d["IMG-URL"].append(img_url)       
        d["price"].append(price_link)      


        
import pandas as pd
df=pd.DataFrame(d)
df.to_csv("Daraz.csv",index=False,encoding="utf-8")



