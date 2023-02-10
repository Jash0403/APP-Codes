import re


pas = input("Enter your password: ")
x = re.search("^[a-z A-Z $#@ 0-9]{6,16}$", pas)

if x:
    print("Valid Password")
else:
    print("Not a Valid Password")
