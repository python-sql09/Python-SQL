# 18.12 Writing transaction data to a file
import datetime
f = open("data/report-file.txt", "a")
f.write("Acme Bank EBP")
f.write("\nDate:" + str(datetime.date.today()))
f.write("\nReport File 0001")
f.close()