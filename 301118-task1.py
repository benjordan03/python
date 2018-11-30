import csv

ifile = open('301118-task1-2.csv','a', newline='')
writeCSV = csv.writer(ifile)

myusername = input("Please enter name\n")
mypassword = input("What's your favourite color?\n")

writeCSV.writerow((myusername, mypassword))
ifile.close()
