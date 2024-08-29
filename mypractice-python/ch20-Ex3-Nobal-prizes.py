# Exercise 3: Nobel Prizes
import json
from collections import Counter

# Load the JSON data
filename = '/home/linuxdeepa/python-sql09/Python-SQL/mypractice-python/data/prize.json'
with open(filename, 'r', encoding='utf-8') as file:
    data = json.load(file)

# Helper function to flatten laureates data
def flatten_laureates(prizes):
    laureates_list = []
    for prize in prizes:
        for laureate in prize.get("laureates", []):
            laureates_list.append((prize['year'], prize['category'], laureate))
    return laureates_list

# Flattened list of laureates
laureates_list = flatten_laureates(data['prizes'])

# 1. Identify the most recent year in the dataset when someone received a Nobel Prize.
most_recent_year = max(prize['year'] for prize in data['prizes'])

# 2. Identify the earliest year when someone received a Nobel Prize.
earliest_year = min(prize['year'] for prize in data['prizes'])

# 3. Identify the category with the highest number of prizes.
category_counts = Counter(prize['category'] for prize in data['prizes'])
most_prizes_category = category_counts.most_common(1)[0]

# 4. Identify the laureate with the highest number of prizes.
laureate_counts = Counter(laureate['id'] for _, _, laureate in laureates_list)
most_awarded_laureate_id = laureate_counts.most_common(1)[0][0]
most_awarded_laureate = next(laureate for _, _, laureate in laureates_list if laureate['id'] == most_awarded_laureate_id)

# 5. Identify the laureate who won the most recent prize in peace.
recent_peace_prize = max((prize for prize in data['prizes'] if prize['category'] == 'peace'), key=lambda x: x['year'])
recent_peace_laureate = recent_peace_prize['laureates'][0]['firstname'] + " " + recent_peace_prize['laureates'][0]['surname']

# 6. Identify the laureate who won the most recent prize in medicine.
recent_medicine_prize = max((prize for prize in data['prizes'] if prize['category'] == 'medicine'), key=lambda x: x['year'])
recent_medicine_laureate = recent_medicine_prize['laureates'][0]['firstname'] + " " + recent_medicine_prize['laureates'][0]['surname']

# 7. Identify the year when the most laureates jointly won the same prize in the same year.
joint_laureates_year = max(data['prizes'], key=lambda x: len(x.get('laureates', [])))

# 8. How many prizes have been given in the economics category?
economics_prizes_count = sum(1 for prize in data['prizes'] if prize['category'] == 'economics')

# 9. How many prizes have been given in the peace category?
peace_prizes_count = sum(1 for prize in data['prizes'] if prize['category'] == 'peace')

# 10. How many prizes have been given in the literature category?
literature_prizes_count = sum(1 for prize in data['prizes'] if prize['category'] == 'literature')

# Display results
print(f"Most recent year a Nobel Prize was awarded: {most_recent_year}")
print(f"Earliest year a Nobel Prize was awarded: {earliest_year}")
print(f"Category with the highest number of prizes: {most_prizes_category[0]} with {most_prizes_category[1]} prizes")
print(f"Laureate with the highest number of prizes: {most_awarded_laureate['firstname']} {most_awarded_laureate['surname']}")
print(f"Laureate who won the most recent prize in peace: {recent_peace_laureate}")
print(f"Laureate who won the most recent prize in medicine: {recent_medicine_laureate}")
print(f"Year with the most laureates jointly winning the same prize: {joint_laureates_year['year']} with {len(joint_laureates_year['laureates'])} laureates")
print(f"Number of prizes in the economics category: {economics_prizes_count}")
print(f"Number of prizes in the peace category: {peace_prizes_count}")
print(f"Number of prizes in the literature category: {literature_prizes_count}")