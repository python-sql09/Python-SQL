# 21.12 Summing exchange rate and transaction amounts
exchange_rate = [1.25, 2, 1.3, 1.18]
transaction_amt = (5, 6, 7, 8)
print(exchange_rate)
print(transaction_amt)
map_iterator = map(lambda x, y: x * y, exchange_rate, transaction_amt)
map_list= list(map_iterator)
print(map_list)