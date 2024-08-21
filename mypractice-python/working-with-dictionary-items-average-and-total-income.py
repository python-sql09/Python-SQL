# 10.8 Working with dictionary items
yearly_revenue = {
2017 : 1000000,
2018 : 1200000,
2019 : 1250000,
2020 : 1100000,
2021 : 1300000,
}
total_income = \
yearly_revenue[2017]+yearly_revenue[2018]+yearly_revenue[2019]+yearly_revenue[2020]+yearly_revenue[2021]
average_income = total_income/5
print(total_income)
print(average_income)