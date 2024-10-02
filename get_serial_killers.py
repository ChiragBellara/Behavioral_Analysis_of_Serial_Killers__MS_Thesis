from selenium import webdriver
from selenium.webdriver.common.by import By
import chromedriver_binary
import csv
import traceback
import pandas as pd
import shutil
import glob


class Get_Data:

    def __init__(self) -> None:
        self.driver = webdriver.Chrome() 
        self.WEBSITES = []

    def write_file(self, rows, writer):
        write_format = []
        for row in rows:
            cells = row.find_elements(By.TAG_NAME, 'td')
            write_format.append([cell.text for cell in cells])
            out = []
            for cell in cells:
                out.append(cell.text)
            try:
                if len(out) > 1:
                    if "-" in out[3] or "+" in out[3] or "?" in out[3]:
                        cleaned_output = out[3].replace("+", "").replace("?", "").strip()
                        out[3] = cleaned_output
                        write_format.append(out)
                    else:
                        if int(out[3]) >= 3:
                            cleaned_output = out[3].strip()
                            out[3] = int(cleaned_output)
                            write_format.append(out)
                else:
                    write_format.append(out)
            except ValueError:
                print(out)    
        writer.writerows(write_format)

    def get_websites(self):
        print("Getting Websites to Scrape START")
        self.driver.get("https://murderpedia.org/index-by-country.htm")
        elems = self.driver.find_element(By.ID, "table4").find_elements(By.XPATH, "//tbody/tr")
        for e in elems:
            cells = e.find_elements(By.XPATH, "//td/p/font/b/a")
            self.WEBSITES.extend([cell.get_attribute('href') for cell in cells])
            break
        print(len(self.WEBSITES), " Websites Found. Scraping Completed.")
        self.create_csv()

    def create_csv(self):
        for WEBSITE in self.WEBSITES:
            print("Reading ", WEBSITE)
            file_name = "data/" + WEBSITE.split("/")[-1].replace(".htm", "") + ".csv"
            try:
                with open(file_name, "w") as file:
                    writer = csv.writer(file, delimiter=',')
                    self.driver.get(WEBSITE)
                    try:
                        rows = self.driver.find_element(By.ID, "table2").find_elements(By.XPATH, '//tbody/tr/td/font/div/table/tbody/tr')
                        print("Writing ", file_name)
                        self.write_file(rows, writer)
                    except:
                        print("EXCEPTION")
                        rows = self.driver.find_element(By.ID, "table4").find_elements(By.XPATH, '//tbody/tr')
                        print("Writing ", file_name)
                        self.write_file(rows, writer)
                file.close()   
            except Exception:
                traceback.print_exc()
                break
        self.driver.close()
        print("CSV's ready")
        self.combine_csv()
    
    def combine_csv(self):
        print("Combining CSV's START")
        writer = pd.ExcelWriter('Serial_Killers.xlsx')
        i = 0
        for file_name in glob.glob("data/*.csv"):
            i += 1
            df = pd.read_csv(file_name, skip_blank_lines=True, encoding='unicode_escape').drop_duplicates()
            sheet_name = file_name.split("\\")[1].replace(".csv","").capitalize()
            df.to_excel(writer,sheet_name=sheet_name)
        writer._save()
        print(i, " CSV's combined into Serial_Killers.xlsx")
        print("Deleting CSV's")
        shutil.rmtree("data")
        print("All Steps Completed!")


if __name__ == "__main__":
    obj = Get_Data()
    obj.get_websites()