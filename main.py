# CABATO, M., REGACHO, R., VICENTE, J.

from mod1 import *
from mod2 import *

print("\n")
sched = []
chosen = []
inchosen = []
off_limits = []
layout1 = "{0:>0}{1:^115}{2:>0}"
layout2 = "{0:<15}{1:<25}{2:<15}{3:>25}{4:<25}"
layout3 = "{0:>0}{1:<0}{2:>20}"
cls = lambda: print('\n'*100)

print(layout1.format("","Personal Information",""))
last_name = input("Last Name:\t\t\t").upper()
first_name = input("First Name:\t\t\t").upper()
middle_name = input("Middle Name:\t\t").upper()
address = input("Permanent Address:\t").capitalize()
age = int(input("Age:\t\t\t\t"))
birth_date = input("Birth Date:\t\t\t").capitalize()
sex = input("Gender:\t\t\t\t").capitalize()
telnum = input("Telephone Number:\t")
phone = input("Mobile Number:\t\t")
email = input("Email Address:\t\t")
rlgn = input("Religion:\t\t\t").capitalize()
ctznshp = input("Citizenship:\t\t").capitalize()
status = input("Civil Status:\t\t").capitalize()
birth_place = input("Birth Place:\t\t").capitalize()
print("\n")
print(layout1.format("","Academic Information",""))
college = input("College:\t\t\t").upper()
degree = input("Degree Program:\t\t").upper()
year =(input("Year:\t\t\t\t"))
id = int(input("ID Number:\t\t\t"))

name = last_name + ", " + first_name
file_name = name + ".txt"
name1 = last_name + ", " + first_name + " " + middle_name

f = open("Student Data.txt", "w")
f.write("\n")
f.write(layout1.format("","Student Enrollment Record",""))
f.write("\n------------------------------------------------------------------------------------------------------------------------")
f.write(layout2.format("\nName: ", name1, "", "College: ", college))
f.write(layout2.format("\nID Number: ", id, "", "Year: ", year))
f.write(layout2.format("\nAddress: ", address, "", "Degree Program: ", degree))
f.write(layout2.format("\nAge: ", age, "", "Birth Date: ", birth_date))
f.write(layout2.format("\nGender: ", sex, "", "Contact Number: ", telnum))
f.write(layout2.format("\nEmail: ", email, "", "Civil Status: ", status))
f.write("\n------------------------------------------------------------------------------------------------------------------------\n\n")
f.close()

print("\n")
print(layout1.format("","Schedule Selection",""))
choice = int(input("Student Status?\t 1 - Regular | 2 - Irregular\n"))

if choice == 1:
   regular(file_name)

elif choice == 2:
   initial(chosen, inchosen)
   irregular(chosen, cls, sched, layout1, layout3, off_limits, inchosen, file_name)