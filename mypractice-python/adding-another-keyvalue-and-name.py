# 10.2 Adding another key value and name
accounts_dict = dict()
accounts_dict['X10000'] = 'Anita'   #Assign key X10000 and value Anita
accounts_dict['X10002'] = 'Michael' #Assign key X10002 and value Michael
accounts_dict['X10003'] = 'Nia'     #Assign key X10003 and value Nia
# Keep in mind that a dictionary cannot include the same key in more than one record. As
# such, when this listing is executed, the fourth item does not get added as a new element.
# Instead, it updates the previous record that had the same key.
accounts_dict['X10003'] = 'Kyra'    #Assign key X10003 and value Kyra
print(accounts_dict)

