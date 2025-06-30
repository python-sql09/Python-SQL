# -------------------------------------------------------------------------------------------
# Project Name: Burger Shop Process Project
# Author      : Deepa Ponnusamy
# Email       : kpdeepa1980@gmail.com,
# GitHub      : https://github.com/python-sql09/Python-SQL/tree/main/myprojects/2024_Federal_Income_Tax_Calculator_Single_Filers
# Date        : August 15, 2024
# Description : The Company Stocks Logger is a user-friendly Python application designed to help
#              users record and manage stock purchase data for different companies. Built with a
#              graphical interface using tkinter, this tool allows users to input the company
#              name, purchase date, and number of shares in a structured form.
#  --------------------------------------------------------------------------------------------------
# 2024 Tax Rates
import tkinter as tk
from tkinter import messagebox
import csv
import os
import pandas as pd
from datetime import datetime

def save_data():
    company = entry_company.get()
    date = entry_date.get()
    shares = entry_shares.get()

    if not company or not date or not shares:
        messagebox.showwarning("Input Error", "All fields are required.")
        return

    try:
        datetime.strptime(date, '%Y-%m-%d')
    except ValueError:
        messagebox.showerror("Date Error", "Date must be in YYYY-MM-DD format.")
        return

    with open('company-stocks.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        if os.stat('company-stocks.csv').st_size == 0:
            writer.writerow(['Company Name', 'Purchase Date', 'Shares'])
        writer.writerow([company, date, shares])

    convert_to_excel()
    messagebox.showinfo("Success", "Data saved to CSV and Excel.")
    entry_company.delete(0, tk.END)
    entry_date.delete(0, tk.END)
    entry_shares.delete(0, tk.END)

def convert_to_excel():
    df = pd.read_csv('company-stocks.csv')
    df.to_excel('company-stocks.xlsx', index=False)

# GUI Setup
root = tk.Tk()
root.title("Company Stocks Logger")
root.geometry("400x250")

tk.Label(root, text="Company Name").pack()
entry_company = tk.Entry(root, width=50)
entry_company.pack()

tk.Label(root, text="Purchase Date (YYYY-MM-DD)").pack()
entry_date = tk.Entry(root, width=50)
entry_date.pack()

tk.Label(root, text="Number of Shares").pack()
entry_shares = tk.Entry(root, width=50)
entry_shares.pack()

tk.Button(root, text="Save Entry", command=save_data).pack(pady=10)

root.mainloop()
