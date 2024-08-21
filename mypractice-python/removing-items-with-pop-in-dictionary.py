# 10.18 Removing items with calls to pop()
acct_list = {
"100001" : "Federica, Yolane",
"100002" : "Celestine, Kirbee",
"100003" : "Paton, Riannon",
"100004" : "Abbot, Gilligan",
"100005" : "Dorine, Chandra",
"100006" : "Natica, Ginnie",
"100007" : "Sperling, Lucille",
"100008" : "Kermit, Iseabal",
"100009" : "Kat, Tori",
"100010" : "Estella, Cristine",
"100011" : "Pauly, Genovera",
"100012" : "Idelia, Beverley",
"100013" : "Nickola, Nessie",
"100014" : "Baudin, Jasmina",
"100015" : "Bates, Lily",
"100016" : "Martguerita, Keelia",
"100017" : "Kirbee, Katharina",
"100018" : "Camden, Eadie",
"100019" : "Iphlgenia, Roberta",
"100020" : "Saint, Joelly",
"100021" : "Lowry, Eadie",
"100022" : "Keelia, Tani",
"100023" : "Philoo, Darlleen",
"100024" : "Artie, Ginnie",
"100025" : "Ajay, Roseline",
"100026" : "Frodi, Brandise",
"100027" : "Daveta, Dorene",
"100028" : "Liebermann, Paulita",
"100029" : "Zola, Wynne",
"100030" : "Heisel, Sue",
"100031" : "Sigfrid, Jsandye",
"100032" : "Kimmie, Jean",
"100033" : "Muriel, Merle",
"100034" : "Viddah, Nelle",
"100035" : "Lewes, Selia",
"100036" : "Lemuela, Marita",
"100037" : "Kalinda, Tatiania",
"100038" : "Firmin, Desirae",
"100039" : "Casimir, Nita",
"100040" : "Pillsbury, Stevana",
"100041" : "Willie, Ira",
"100042" : "Connelly, Etta",
"100043" : "Cookie, Joleen",
"100044" : "Himelman, Belva",
"100045" : "Annabella, Ketti",
"100046" : "Wandie, Brynna",
"100047" : "Gaynor, Emelina",
"100048" : "Christal, Tonia",
"100049" : "Lowry, Wilma",
"100050" : "Sholley, Corene"
}
newlist = dict()
for key,value in list(acct_list.items()):
    if int(key) > 100025:
        newlist[key] = value
        acct_list.pop(key)
print("List after 100025", newlist)
print("=======================")
print("List before 100025", acct_list)
acct_IDs = acct_list.keys()
acct_names = acct_list.values()
print(acct_IDs)
print(acct_names)
acct_IDs = newlist.keys()
acct_names = newlist.values()
print(acct_IDs)
print(acct_names)