# 8.10 Slicing a set of lists with corresponding data
trans_date=['2021-04-03','2021-12-03',
            '2021-13-03','2021-15-03','2021-22-03',
            '2021-25-03','21-30-03','2021-03-04']
trans_amt=[2.45,4.50,5.75,10.00,12.30,4.25,15.25,16.20]
print(trans_date)
input_to_date = input("What end date would you like to see all the transaction amounts from? (format: YYYY-DD-MM): ")
trans_date_to = trans_date.index(input_to_date)
print(trans_date_to)
print(trans_amt[0: int(trans_date_to)+1])
