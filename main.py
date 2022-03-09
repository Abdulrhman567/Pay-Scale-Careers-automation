from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd

CHROME_DRIVER_PATH = "C:\Development\chromedriver.exe"


def get_data_in_csv():
    """Stores all Pay Scale Careers statistics into a CSV file"""
    pay_scale_dict = {title: [] for title in all_titles_list}
    row = []
    for value in all_values_list:
        row.append(value)
        if len(row) == 6:
            for index, row_value in enumerate(row):
                pay_scale_dict[all_titles_list[index]].append(row_value)
            row.clear()

        pay_scale_df = pd.DataFrame(pay_scale_dict)
        pay_scale_df.to_csv('Pay-Scale-Careers.csv')


# PayScale Careers Bot
driver = webdriver.Chrome(executable_path=CHROME_DRIVER_PATH)
driver.get(url="https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors")

# All Careers and Pay Scale Titles
all_titles = driver.find_elements(By.CLASS_NAME, 'data-table__header')
all_titles_list = [title.text for title in all_titles]

# All Careers and Pay Scale Data
all_values = driver.find_elements(By.CLASS_NAME, 'data-table__value')
all_values_list = [value.text for value in all_values]

if __name__ == "__main__":
    # get all the data and put it into CSV file
    get_data_in_csv()

    driver.close()
