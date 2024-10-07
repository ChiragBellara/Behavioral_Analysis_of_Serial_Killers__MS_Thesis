from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary
import csv

driver = webdriver.Chrome()  # or webdriver.Firefox()

driver.get("https://murderpedia.org/usa/alabama.htm")
# rows = driver.find_element(By.ID, "table2").find_elements(By.XPATH, '//tbody/tr/td/font/div/table/tbody/tr')
rows = driver.find_element(By.ID, "table2").find_elements(By.TAG_NAME, 'a')
links = [link.get_attribute('href') for link in rows]
# for row in rows:
#     cells = row.find_elements(By.TAG_NAME, 'td')
#     if len(cells) > 1:
#         link = cells[1].find_element(By.TAG_NAME, 'a')
#         href = link.get_attribute('href')
#         links.append(href)



print(links)
driver.close()