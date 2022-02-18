from selenium import webdriver 
from bs4 import BeautifulSoup
import time 
import csv 

start_url = "https://www.nasa.gov/"
browser = webdriver.Chrome("C:/DHRUV/Whitehat Projects/assignment projects/Web scrapping/chromedriver_win32/chromedriver.exe")
browser.get(start_url)
time.sleep(10)

headers = ["Planet","Name","Distance","Mass","Radius"]
star_data = []


def Scrap():
    soup = BeautifulSoup(browser.page_source, "html.parser")
    for tr_tag in soup.find_all("tr"):
        td_tags = tr_tag.find_all("td")
        temp_list = []
        for index,td_tags in enumerate(td_tags):
            temp_list.append(td_tags.contents[0])
            print(td_tags.contents[0])
    star_data.append(temp_list)

with open ("planets_stars.csv","w") as f:
    csvwritter  = csv.writer(f)
    csvwritter.writerow(headers)
    csvwritter.writerow(star_data)

Scrap()
