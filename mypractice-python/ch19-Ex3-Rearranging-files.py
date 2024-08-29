# Exercise 3: Rearranging Files
# •• Open and read a CSV file.
# •• Count the number of rows in the file.
# •• Split the file into three separate CSV files so that each file includes approximately
# the same number of rows.
# •• Reassemble the three CSV files into a new file with the pieces in a different order
# from the original.
# •• For example, if the original is split into Part 1, Part 2, and Part 3, the new file
# could contain the same content in the order Part 3, Part 1, Part 2.
import csv
import os

def count_rows_in_file(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        return sum(1 for row in reader)

def split_csv_file(file_path, parts=3):
    with open(file_path, 'r') as file:
        reader = list(csv.reader(file))
        header = reader[0]
        rows = reader[1:]
        total_rows = len(rows)
        part_size = total_rows // parts
        
        file_parts = []
        for i in range(parts):
            start_index = i * part_size
            if i == parts - 1:  # Last part takes any remaining rows
                end_index = total_rows
            else:
                end_index = start_index + part_size

            part_file_name = f"{file_path}_part{i + 1}.csv"
            with open(part_file_name, 'w', newline='') as part_file:
                writer = csv.writer(part_file)
                writer.writerow(header)  # Write the header to each part
                writer.writerows(rows[start_index:end_index])

            file_parts.append(part_file_name)
    
    return file_parts

def reassemble_csv_files(output_file_path, file_parts):
    order = [2, 0, 1]  # Example new order: Part 3, Part 1, Part 2
    with open(output_file_path, 'w', newline='') as output_file:
        writer = csv.writer(output_file)
        
        for i, part_file in enumerate(file_parts):
            with open(file_parts[order[i]], 'r') as part:
                reader = csv.reader(part)
                if i == 0:
                    writer.writerow(next(reader))  # Write header only once
                else:
                    next(reader)  # Skip the header for subsequent parts
                writer.writerows(reader)
    
    print(f"Reassembled file saved as {output_file_path}")

def main():
    original_file = '/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/company-stocks.csv'
    output_file = '/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/rearranged-stocks.csv'
    
    # Count the rows in the original file
    total_rows = count_rows_in_file(original_file)
    print(f"The original file has {total_rows} rows.")
    
    # Split the original file into 3 parts
    file_parts = split_csv_file(original_file)
    print(f"File split into parts: {file_parts}")
    
    # Reassemble the parts into a new file in a different order
    reassemble_csv_files(output_file, file_parts)
    
    # Cleanup: Optionally remove the part files after reassembling
    for part_file in file_parts:
        os.remove(part_file)
    print("Temporary part files removed.")

if __name__ == "__main__":
    main()