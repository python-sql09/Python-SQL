# 18.13 Writing a list to a file
customers = ["Ax Lodevick", "Frank Prys", "Ania Hearle",
"Justus Bodker", "Clementius Druce", "Ganny Penwright",
"Alick Rens", "Gwen Drewitt", "Jessie Wychard",
"Brina Elliss", "Derril Damiral", "Jade Cutajar",
"Brannon Goldsmith", "Valentin Salmons", "Tull Rennix",
"Quintina Whanstall", "Lev Frunks", "Doris Heskin",
"Idalina Moro", "Gillie Ledram"
]
def write_list_2_file(input_list,input_file_path):
    f = open(input_file_path, "a")
    for name in input_list:
        name = "\n"+name
        f.write(name)
    f.close()
write_list_2_file(customers,"/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/Customers.txt")