import csv

ifile = open('username.csv','r')
readCSV = csv.reader(ifile)

myusername = input("Please enter username\n")
mypassword = input("Please enter password\n")

found = "no"

for row in readCSV:
    username = row[0]
    password = row[1]
    fname = row[2]
    sname = row[3]

    if username == myusername:
        found = "yes"
        if password == mypassword:
            print("Welcome!")
        else:
            print("You seem to have entered the wrong password")

if found == "no":
    print("No details matching yours exist")

ifile.close()
