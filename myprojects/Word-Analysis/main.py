# 2. The main function to run function to read a JSON file
from lib import *
dataset = read_json_file("reviews.json") #read file
print(dataset[0])