from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary
import traceback
import pandas as pd
from selenium.common.exceptions import NoSuchElementException
from IPython.display import display, HTML


def find_element_by_multiple_ids(driver, *ids):
    for element_id in ids:
        try:
            return driver.find_element(By.ID, element_id)
        except NoSuchElementException:
            pass


driver = webdriver.Chrome()
FILE = 'CompleteFiles/Killers.xlsx'
xls = pd.ExcelFile(FILE)
row_list = []
for sheet in xls.sheet_names:
    df = pd.read_excel(FILE, sheet_name=sheet)
    print("READING: ", sheet)
    try:
        with open("CompleteFiles/not_found.txt", 'a') as nf:
            for (i, row) in df.iterrows():
                driver.get(row['Link'])
                try:
                    rows = driver.find_elements(
                        By.XPATH, "//*[contains(text(), 'Serial killer')]")
                    for r in rows:
                        if r.text.strip() != "":
                            newRow = {
                                'Name': row['Name'],
                                'Date': row['Date'],
                                'Link': row['Link'],
                                'Victims': row['Victims'],
                                'Location': row['Location']
                            }
                            row_list.append(newRow)
                            print(len(row_list), newRow)
                    # table_elem = find_element_by_multiple_ids(
                    #     driver, "table4", "table8", "table9")
                    # rows = table_elem.find_elements(By.XPATH, '//tbody/tr')
                    # for r in rows:
                    #     cells = r.find_elements(By.TAG_NAME, 'td')
                    #     for cell in cells:
                    #         if i == 4 or i == 13:
                    #             with open("test.txt", "a") as test:
                    #                 test.write(cell.text + "\n")
                    #                 test.write(
                    #                     "++++++++++++++++++++++++++++++++++++++++++++++++\n")
                    #         if "Classification: Serial Killer" in cell.text:
                    #             print("SERIAL KILLER: ", row["Link"])

                except:
                    nf.write(row['Link'] + "\n")
            # rows = driver.find_element(
            #     By.ID, "table4").find_elements(By.TAG_NAME, 'a')
            # links = []
            # for row in rows:
            #     links.append(row.get_attribute('href'))
            # print(links)
            # writer.writerows(links)
        nf.close()
    except Exception:
        traceback.print_exc()
    # test.close()
driver.close()

just_sk = pd.DataFrame(row_list)
just_sk.to_csv("CompleteFiles/DONE.csv")
