# Exercise 2: Separating the High from the Low
# Account balances
acct_bals = {
    100000: 48213,
    100001: 51734,
    100002: 57182,
    100003: 80223,
    100004: 126407,
    100005: 6906,
    100006: 31751,
    100007: 103604,
    100008: 56302,
    100009: 102858,
    100010: 62231,
    100011: 74452,
    100012: 114445,
    100013: 116356,
    100014: 93835,
    100015: 117400,
    100016: 86871,
    100017: 110701,
    100018: 140843,
    100019: 70847,
    100020: 121284,
    100021: 65575,
    100022: 58480,
    100023: 91149,
    100024: 16864,
    100025: 95236,
    100026: 112596,
    100027: 13542,
    100028: 149743,
    100029: 64281,
    100030: 112104,
    100031: 148971,
    100032: 22793,
    100033: 111465,
    100034: 16781,
    100035: 36179,
    100036: 108157,
    100037: 40644,
    100038: 20916,
    100039: 9413,
    100040: 20919,
    100041: 147567,
    100042: 111814,
    100043: 54442,
    100044: 7364,
    100045: 90014,
    100046: 18668,
    100047: 125017,
    100048: 8983,
    100049: 109160
}

# Separate into two dictionaries: low_balances and high_balances
low_balances = {}
high_balances = {}

for account, balance in acct_bals.items():
    if balance < 100000:
        low_balances[account] = balance
    else:
        high_balances[account] = balance

# Print the number of entries and the average balance for low_balances
low_count = len(low_balances)
low_total = sum(low_balances.values())
low_avg = sum(low_balances.values()) / low_count if low_count > 0 else 0
print(f"Low Balances: {low_count} entries, Total balance: {low_total}, Average balance: ${low_avg:.2f}")
print(low_balances)
# Print the number of entries and the average balance for high_balances
high_count = len(high_balances)
high_total = sum(high_balances.values())
high_avg = sum(high_balances.values()) / high_count if high_count > 0 else 0
print(f"High Balances: {high_count} entries, Total balance: {high_total}, Average balance: ${high_avg:.2f}")
print(high_balances)