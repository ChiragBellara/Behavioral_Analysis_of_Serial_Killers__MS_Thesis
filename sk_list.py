from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary
import csv

WEBSITE_LIST = [
   "https://skdb.fandom.com/wiki/Category:Serial_Killers_from_United_States",
   "https://skdb.fandom.com/wiki/Category:Serial_Killers_from_United_States?from=BRINKLEY+Sidney",
   "https://skdb.fandom.com/wiki/Category:Serial_Killers_from_United_States?from=CUTLIP+Jeffrey+Paul",
   "https://skdb.fandom.com/wiki/Category:Serial_Killers_from_United_States?from=GILES+Bernard+Eugene",
   "https://skdb.fandom.com/wiki/Category:Serial_Killers_from_United_States?from=HUMPHREY+George",
   "https://skdb.fandom.com/wiki/Category:Serial_Killers_from_United_States?from=Long+Island+Serial+Killer",
   "https://skdb.fandom.com/wiki/Category:Serial_Killers_from_United_States?from=NOLAN+Dempsey",
   "https://skdb.fandom.com/wiki/Category:Serial_Killers_from_United_States?from=RUNGE+Paul+Frederick",
   "https://skdb.fandom.com/wiki/Category:Serial_Killers_from_United_States?from=THORNBURG+Jason+Alan"
]


driver = webdriver.Chrome()  # or webdriver.Firefox()

with open("serial_killers.csv", "a") as file:
    writer = csv.writer(file, delimiter=',')
    for site in WEBSITE_LIST:
        driver.get(site)
        name_elements = driver.find_elements(By.XPATH ,"//li[@class='category-page__member']")
        for names in name_elements:
            print(names.text)
            writer.writerow(names.text)
    
    driver.close()
    file.close()