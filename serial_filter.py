from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary


driver = webdriver.Chrome()
driver.get("https://murderpedia.org/usa/alabama.htm")

rows = driver.find_elements(By.XPATH, '//table/tbody/tr')
filtered_hrefs = []

for row in rows:
    cells = row.find_elements(By.TAG_NAME, 'td')
    if len(cells) >= 3:
        try:
            print(cells)
            # third_value = int(cells[2].text.strip())
            # if third_value > 3:
            #     link = cells[1].find_element(By.TAG_NAME, 'a')
            #     href = link.get_attribute('href')
            #     filtered_hrefs.append(href)
        except ValueError:
            continue

for href in filtered_hrefs:
    print(href)

driver.quit()
