# 10.10 Printing and summing a variable number of items
yearly_revenue = {
2017 : 1000000,
2018 : 1200000,
2019 : 1250000,
2020 : 1100000,
2021 : 1300000,
}
total_income = 0
for year_id in yearly_revenue.keys():
    total_income+=yearly_revenue[year_id]
    print(year_id, yearly_revenue[year_id])
print(total_income)
print(total_income/len(yearly_revenue))