# 8.17 Cleaning up a list
input_list = ["Haythem", "Mike", 1, "Layla",
"Livia", "Layla", 2, 1, 2, 3, "Mike",
"Jesse", "Haythem"]
print(input_list)
input_list.remove(1)
input_list.remove(2)
input_list.remove("Layla")
input_list.remove("Mike")
input_list.remove("Haythem")
print(input_list)