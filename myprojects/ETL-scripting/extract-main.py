# --------------------------------------------------------------------------------
# Project Name: ETL Transformation with Script Project
# Author      : Deepa Ponnusamy
# Email       : kpdeepa1980@gmail.com,
# GitHub      : https://github.com/python-sql09/Python-SQL/tree/main/myprojects/ETL-scripting
# Date        : March 27, 2025 to May 3, 2025
# Description : Extract CSV file
# --------------------------------------------------------------------------------
from extract import extract
e = extract()
dataset = e.fromCSV(file_path="got_chars.csv")
for row in dataset:
    print(row)
