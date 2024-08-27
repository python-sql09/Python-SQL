# Exercise 2: Company Stocks
# In this exercise create a file called company-­stocks.csv that includes three columns:
# •• company_name: The name of the company
# •• purchase_date: The purchase date of the stock
# •• shares: The number of shares purchased
import csv

def collect_company_data():
    company_data = []
    for i in range(5):
        print(f"Enter details for company {i + 1}:")
        company_name = input("Company Name: ")
        purchase_date = input("Purchase Date (YYYY-MM-DD): ")
        shares = input("Number of Shares: ")

        # Add the company's information to the list
        company_data.append([company_name, purchase_date, shares])

    return company_data

def write_to_csv(file_path, data):
    try:
        with open(file_path, 'a', newline='') as file:
            writer = csv.writer(file)
            writer.writerows(data)
        print(f"Data successfully written to {file_path}.")
    except Exception as e:
        print(f"An error occurred while writing to the file: {e}")

def display_csv_contents(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.reader(file)
            print("\nCurrent contents of the file:")
            for row in reader:
                print(', '.join(row))
    except FileNotFoundError:
        print("File not found. Please provide a valid file path.")
    except Exception as e:
        print(f"An error occurred while reading the file: {e}")

def main():
    file_path = '/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/company-stocks.csv'
    
    # Collect data from the user
    company_data = collect_company_data()
    
    # Write data to the CSV file
    write_to_csv(file_path, company_data)
    
    # Display the contents of the CSV file
    display_csv_contents(file_path)

if __name__ == "__main__":
    main()